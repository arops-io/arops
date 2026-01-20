
# Adaptive Resilience Operations (AROps)

**Adaptive Resilience Operations for AI Systems**

> Because the future is probabilistic, our operations must be adaptive.

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![PRE Framework](https://img.shields.io/badge/Framework-PRE-teal.svg)](https://arops.dev/manifesto)

---

## The Problem

Traditional chaos engineering asks: *"Does it break?"*

That question made sense for deterministic systems. Servers either respond or they don't. Databases either return data or they time out. Failures are binary, observable, and reproducible.

AI systems don't work that way.

When an LLM hallucinates, it doesn't crash—it confidently returns the wrong answer. When a multi-agent workflow drifts, no alert fires. When errors propagate through an agent chain, each step can *amplify* the uncertainty rather than contain it.

You can't test for "broken" when the system never technically breaks.

---

## A Different Question

**Probabilistic Resilience Engineering (PRE)** asks a fundamentally different question:

> *"How does the probability distribution of system behavior shift when X becomes unreliable?"*

This isn't an iteration on chaos engineering. It's a paradigm shift—from testing for failure to measuring behavioral drift, from binary outcomes to probabilistic resilience.

**AROps** is the operational discipline that puts PRE into practice.

---

## What AROps Provides

### The Physics of Failure

PRE introduces measurement where intuition used to live:

| Metric | What It Measures | Why It Matters |
|--------|------------------|----------------|
| **Cascade Amplification (A_C)** | Does error grow or shrink as it propagates? | A_C > 1 means your system amplifies errors. A_C < 1 means it contains them. |
| **Coherence Tension Index (CTI)** | Is the system hiding stress? | High confidence + high hidden work = fragile equilibrium. The system looks healthy while exhausting capacity. |

The new SLA isn't uptime. It's **A_C < 1 under stress.**

### Semantic Circuit Breakers

Traditional circuit breakers trip on latency or error rates. Semantic Circuit Breakers trip on *meaning drift*—detecting when uncertainty amplifies across agent boundaries before it causes downstream damage.

They measure, not judge. Observable signals like embedding distance, entity novelty, and confidence inflation don't require trusting AI to evaluate AI.

### Hallucination Cascade Detection

A hallucination cascade occurs when one agent's confabulation propagates through a multi-agent workflow, with each step potentially amplifying the error. AROps provides tools to inject controlled hallucinations and measure how your system responds.

Does it contain the error? Or does it amplify it?

---

## The Three Laws of PRE

These are constraints, not guidelines. They shape everything else.

**I. Trust Over Truth**

The question is not "Is this answer correct?" The question is "Is this workflow trustworthy?"

Correctness is a property of a single output. Trust is a property of a system over time. You cannot verify every LLM response. You *can* verify that the architecture enforces transparency, auditability, and containment.

**II. Architecture Over Model**

Do not rely on the model to be safe. Rely on the architecture encapsulating it.

Safety is not a guardrail around the model. It is the signal path through which the model operates. An agent that can act without governance is not "unmonitored"—it is architecturally broken.

**III. Cost Is a Reliability Metric**

Financial exhaustion is a reliability incident.

A retry storm that burns $50,000 in API calls has failed—even if every response was "correct." Economic signals are first-class citizens in the governance loop.

---

## Quick Start

### See It In Action

Visit the [Cascade Amplification Sandbox](https://arops.dev/demo) to watch a hallucination propagate through a loan approval pipeline—and see the math that detects it.

### Run the Proof-of-Life

```bash
# Clone the repository
git clone https://github.com/arops-io/arops.git
cd arops/examples

# Run the hello world demo (zero dependencies)
python hello_world.py
```

You'll see three scenarios demonstrating CASCADE_AMP in action:

| Scenario | CASCADE_AMP | Result |
|----------|-------------|--------|
| Normal operation | **0.74** | ✅ CONTAINED — system stable |
| Hallucination (with damping) | **0.06** | ✅ DAMPED — cascade interrupted |
| Hallucination (no damping) | **1.35** | ⚠️ AMPLIFIER — error is growing |


### Read the Manifesto

The [PRE Manifesto](https://arops.dev/manifesto) provides the full theoretical foundation—the physics, the measurement framework, and the call to action.

---

## Repository Structure

```
arops/
├── README.md                 # You are here
├── LICENSE                   # Apache 2.0
├── CONTRIBUTING.md           # How to contribute
├── examples/
│   ├── hello_world.py        # PRE proof-of-life demo
│   └── cascade-sandbox.html  # Interactive visualization
├── website/
│   ├── index.html            # arops.dev landing page
│   ├── manifesto.html        # PRE Manifesto (canonical)
│   └── demo.html             # Cascade sandbox demo
└── docs/
    └── MANIFESTO.md          # Manifesto source (links to canonical)
```

---

## Why This Matters

For fifteen years, chaos engineering has been a bolt-on—testing what was already built, verifying what was already deployed. It served us well for deterministic systems.

But we are now operating non-deterministic AI agents using operational playbooks designed for the monoliths of 2010. We are repeating the mistakes of the past, at a velocity and scale that makes manual remediation impossible.

PRE is not a replacement for chaos engineering. It's what chaos engineering becomes when the systems it tests are no longer deterministic.

The best engineers have been practicing probabilistic resilience intuitively for years—treating uncertainty as a first-class citizen, building containment into architecture, measuring behavioral drift instead of just uptime.

We're not inventing a discipline. We're naming one that already exists.

---

## Contributing

We welcome contributions from practitioners, researchers, and anyone building AI systems that need to be trustworthy under stress.

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:

- Submitting chaos agents and detection mechanisms
- Improving the measurement framework
- Proposing changes to PRE theory
- Documentation and examples

This is an open invitation. The framework will evolve through practice, not proclamation.

---

## Community

- **Website:** [arops.dev](https://arops.dev)
- **Manifesto:** [arops.dev/manifesto](https://arops.dev/manifesto)
- **Demo:** [arops.dev/demo](https://arops.dev/demo)
- **Contact:** hello@arops.dev

---

## License

Apache 2.0 — See [LICENSE](LICENSE) for details.

---

<p align="center">
  <em>Probabilistic Resilience Engineering</em><br>
  <strong>Because the future is probabilistic, our operations must be adaptive.</strong>
</p>
