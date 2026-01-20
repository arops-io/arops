#!/usr/bin/env python3
"""
PRE Hello World: Cascade Entropy Detection & Damping
=====================================================

This script demonstrates the core concepts of Probabilistic Resilience Engineering:

1. CASCADE AMPLIFICATION (A_c): Is the error growing or shrinking?
   - A_c > 1.0 = Entropy Amplifier (unstable, the lie is growing)
   - A_c < 1.0 = Entropy Damper (stable, system is recovering)

2. SEMANTIC DAMPING: Circuit breakers that stop low-confidence signals

Run: python hello_world.py
No dependencies required (uses Python stdlib only)

Author: Jason Doffing | https://arops.dev
License: Apache 2.0
"""

import math
from dataclasses import dataclass

# ==============================================================================
# CONFIGURATION
# ==============================================================================

CONFIDENCE_THRESHOLD = 0.70  # Signals below this get damped
CASCADE_AMP_CRITICAL = 1.0   # Above this = entropy amplifier


# ==============================================================================
# DATA STRUCTURES
# ==============================================================================

@dataclass
class AgentOutput:
    """Output from an agent with confidence metadata."""
    content: str
    confidence: float
    agent_id: str


# ==============================================================================
# SIMULATED AGENTS
# ==============================================================================

def agent_researcher(inject_hallucination: bool = False) -> AgentOutput:
    """Agent A: Upstream researcher that might hallucinate."""
    if inject_hallucination:
        # HALLUCINATION: Agent confidently states something false
        return AgentOutput(
            content="Root cause identified: Memory leak in auth-service "
                    "consuming 2.3GB/hour since 3:47 PM.",
            confidence=0.42,  # Low confidence - this is the tell
            agent_id="researcher"
        )
    else:
        # Normal operation: accurate, high-confidence output
        return AgentOutput(
            content="System metrics nominal. CPU at 34%, memory at 61%. "
                    "No anomalies detected in the last 4 hours.",
            confidence=0.94,
            agent_id="researcher"
        )


def agent_analyst(upstream: AgentOutput, apply_damping: bool = False) -> AgentOutput:
    """Agent B: Analyst that processes researcher output."""
    
    # SEMANTIC DAMPING: Check confidence before processing
    if apply_damping and upstream.confidence < CONFIDENCE_THRESHOLD:
        return AgentOutput(
            content=f"[DAMPED] Low-confidence signal rejected. "
                    f"Upstream confidence: {upstream.confidence:.0%}",
            confidence=0.0,  # Signal terminated
            agent_id="analyst"
        )
    
    if upstream.confidence < 0.5:
        # Processing low-confidence input degrades quality further
        return AgentOutput(
            content=f"Based on research: Recommending immediate restart of "
                    f"auth-service to resolve memory leak.",
            confidence=0.31,  # Confidence degraded - cascade amplifying
            agent_id="analyst"
        )
    else:
        # High-confidence input maintains or improves quality
        return AgentOutput(
            content="Analysis complete: System healthy. No action required. "
                    "Next review scheduled in 2 hours.",
            confidence=0.95,  # Confidence maintained/improved - stable system
            agent_id="analyst"
        )


def agent_executor(upstream: AgentOutput, apply_damping: bool = False) -> AgentOutput:
    """Agent C: Executor that takes action based on analyst recommendation."""
    
    # SEMANTIC DAMPING: Check confidence before acting
    if apply_damping and upstream.confidence < CONFIDENCE_THRESHOLD:
        return AgentOutput(
            content=f"[DAMPED] Refusing to execute on low-confidence recommendation. "
                    f"Escalating to human operator.",
            confidence=0.0,  # Action blocked
            agent_id="executor"
        )
    
    if upstream.confidence == 0.0:
        # Already damped upstream
        return AgentOutput(
            content="[BLOCKED] No action taken - upstream signal was damped.",
            confidence=0.0,
            agent_id="executor"
        )
    
    if upstream.confidence < 0.5:
        # Executing on bad recommendation
        return AgentOutput(
            content="EXECUTED: auth-service restarted. "
                    "WARNING: 847 active user sessions terminated.",
            confidence=0.28,  # Very low - cascade has amplified
            agent_id="executor"
        )
    else:
        return AgentOutput(
            content="Acknowledged: No action required. Monitoring continues.",
            confidence=0.96,  # High confidence maintained - healthy system
            agent_id="executor"
        )


# ==============================================================================
# CASCADE METRICS
# ==============================================================================

def calculate_entropy(confidence: float) -> float:
    """
    Shannon entropy: H = -log2(confidence)
    
    Higher confidence = lower entropy (more certain)
    Lower confidence = higher entropy (more uncertain)
    """
    if confidence <= 0:
        return float('inf')
    if confidence >= 1:
        return 0.0
    return -math.log2(confidence)


def calculate_cascade_amp(upstream_conf: float, downstream_conf: float) -> float:
    """
    Cascade Amplification: A_c = H_downstream / H_upstream
    
    A_c > 1.0 = AMPLIFIER (entropy growing, lie spreading)
    A_c < 1.0 = DAMPER (entropy shrinking, system recovering)
    A_c = 1.0 = NEUTRAL (entropy unchanged)
    """
    h_up = calculate_entropy(upstream_conf)
    h_down = calculate_entropy(downstream_conf)
    
    if h_up == 0:
        return 1.0  # No upstream uncertainty
    if h_down == float('inf'):
        return float('inf')  # Complete failure
        
    return h_down / h_up


# ==============================================================================
# DEMO RUNNER
# ==============================================================================

def print_header(title: str):
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


def print_agent_output(output: AgentOutput, label: str):
    conf_bar = "█" * int(output.confidence * 20) + "░" * (20 - int(output.confidence * 20))
    print(f"\n  [{label}] {output.agent_id.upper()}")
    print(f"  Confidence: [{conf_bar}] {output.confidence:.0%}")
    print(f"  Output: {output.content[:70]}...")


def run_scenario(name: str, inject_hallucination: bool, apply_damping: bool):
    """Run a single scenario and display results."""
    
    print_header(name)
    
    # Run the agent chain
    research = agent_researcher(inject_hallucination=inject_hallucination)
    print_agent_output(research, "1")
    
    analysis = agent_analyst(research, apply_damping=apply_damping)
    print_agent_output(analysis, "2")
    
    execution = agent_executor(analysis, apply_damping=apply_damping)
    print_agent_output(execution, "3")
    
    # Calculate cascade metrics
    if execution.confidence > 0 and research.confidence > 0:
        cascade_amp = calculate_cascade_amp(research.confidence, execution.confidence)
        h_upstream = calculate_entropy(research.confidence)
        h_downstream = calculate_entropy(execution.confidence)
    else:
        cascade_amp = 0.0  # Damped - no cascade
        h_upstream = calculate_entropy(research.confidence)
        h_downstream = 0.0
    
    # Display metrics
    print("\n  " + "-" * 50)
    print("  CASCADE METRICS")
    print("  " + "-" * 50)
    print(f"  H_upstream (researcher):   {h_upstream:.2f} bits")
    print(f"  H_downstream (executor):   {h_downstream:.2f} bits")
    print(f"  CASCADE_AMP (A_c):         {cascade_amp:.2f}")
    
    if cascade_amp == 0:
        print("\n  ✅ RESULT: CASCADE BLOCKED — Damping prevented propagation")
    elif cascade_amp > CASCADE_AMP_CRITICAL:
        print(f"\n  ⚠️  RESULT: ENTROPY AMPLIFIER — The lie is growing!")
    else:
        print(f"\n  ✅ RESULT: ENTROPY DAMPER — System is stable")
    
    return cascade_amp


def run_demo():
    """Run the complete PRE demonstration."""
    
    print("""
    ╔═══════════════════════════════════════════════════════════════════════╗
    ║                                                                       ║
    ║   PRE HELLO WORLD: Cascade Entropy Detection & Damping                ║
    ║   Probabilistic Resilience Engineering                                ║
    ║                                                                       ║
    ║   Watch how hallucinations cascade through a 3-agent system,          ║
    ║   and how SEMANTIC DAMPING stops the spread.                          ║
    ║                                                                       ║
    ╚═══════════════════════════════════════════════════════════════════════╝
    """)
    
    # -------------------------------------------------------------------------
    # SCENARIO 1: Normal Operation (Baseline)
    # -------------------------------------------------------------------------
    amp_normal = run_scenario(
        name="SCENARIO 1: Normal Operation",
        inject_hallucination=False,
        apply_damping=False
    )
    
    # -------------------------------------------------------------------------
    # SCENARIO 2: Hallucination WITH Damping (Protected)
    # -------------------------------------------------------------------------
    amp_damped = run_scenario(
        name="SCENARIO 2: Hallucination Injection + Semantic Damping",
        inject_hallucination=True,
        apply_damping=True
    )
    
    # -------------------------------------------------------------------------
    # SCENARIO 3: Hallucination WITHOUT Damping (Cascade)
    # -------------------------------------------------------------------------
    amp_cascade = run_scenario(
        name="SCENARIO 3: Hallucination Injection — NO DAMPING",
        inject_hallucination=True,
        apply_damping=False
    )
    
    # -------------------------------------------------------------------------
    # SUMMARY
    # -------------------------------------------------------------------------
    print("\n")
    print("=" * 70)
    print("  SUMMARY: CASCADE AMPLIFICATION COMPARISON")
    print("=" * 70)
    print(f"""
    ┌─────────────────────────────────────┬─────────────┬─────────────────┐
    │ Scenario                            │ CASCADE_AMP │ Status          │
    ├─────────────────────────────────────┼─────────────┼─────────────────┤
    │ 1. Normal Operation                 │    {amp_normal:5.2f}    │ ✅ DAMPER       │
    │ 2. Hallucination + Damping          │    {amp_damped:5.2f}    │ ✅ BLOCKED      │
    │ 3. Hallucination (no damping)       │    {amp_cascade:5.2f}    │ ⚠️  AMPLIFIER   │
    └─────────────────────────────────────┴─────────────┴─────────────────┘
    """)
    
    print("=" * 70)
    print("  THE TAKEAWAY")
    print("=" * 70)
    print("""
    • A_c > 1.0 → Entropy amplifier. Errors multiply. P1 incoming.
    • A_c < 1.0 → Entropy damper. System self-heals.
    • A_c = 0   → Cascade blocked. Damping caught it.
    
    SEMANTIC DAMPING drops uncertain signals BEFORE they cascade.
    It's a circuit breaker for bullshit.
    
    This isn't about AI safety philosophy.
    It's about not getting paged at 3am.
    
    ───────────────────────────────────────────────────────────────────────
    Learn more:      https://arops.dev
    Full framework:  https://github.com/arops-io/arops
    ═══════════════════════════════════════════════════════════════════════
    """)


if __name__ == "__main__":
    run_demo()