# Contributing to AROps

Thank you for your interest in contributing to AROps and Probabilistic Resilience Engineering (PRE). This project aims to shift how the industry architects and operates AI systems — and we need practitioners, researchers, and builders to make that happen.

## Ways to Contribute

### 🔬 Research & Theory
- Validate or challenge the PRE metrics (CASCADE_AMP, CTI, H_cascade)
- Propose new measurement approaches for semantic drift
- Share empirical data from production AI systems
- Peer review theoretical foundations

### 🛠️ Code & Tools
- Build implementations of PRE metrics in new languages
- Create observability integrations (OpenTelemetry, Datadog, etc.)
- Develop semantic circuit breaker patterns
- Improve existing demos and examples

### 📖 Documentation
- Improve explanations and tutorials
- Add real-world case studies
- Translate documentation
- Fix typos and clarify confusing sections

### 🐛 Bug Reports & Feature Requests
- Report issues with existing code
- Suggest new features or improvements
- Share edge cases that break current implementations

## Getting Started

### 1. Fork and Clone

```bash
git clone https://github.com/arops-io/arops.git
cd arops
```

### 2. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/issue-description
```

### 3. Make Your Changes

- Follow existing code style and conventions
- Add tests for new functionality
- Update documentation as needed

### 4. Submit a Pull Request

- Provide a clear description of the change
- Reference any related issues
- Be responsive to feedback

## Code Standards

### General Principles
- **Clarity over cleverness** — Code should be readable
- **Tested** — New features need tests
- **Documented** — Public APIs need docstrings/comments

### Language-Specific

**TypeScript/JavaScript:**
- Use TypeScript for new code
- Follow existing ESLint configuration
- Prefer async/await over raw promises

**Python:**
- Follow PEP 8
- Use type hints
- Prefer stdlib when possible (minimize dependencies)

## Reporting Issues

When reporting bugs, please include:

1. **Environment** — OS, language version, relevant dependencies
2. **Steps to reproduce** — Minimal example that demonstrates the issue
3. **Expected behavior** — What you expected to happen
4. **Actual behavior** — What actually happened
5. **Logs/errors** — Any relevant error messages or stack traces

## Proposing Changes to PRE Theory

PRE is an evolving framework. If you want to propose changes to the core metrics or theoretical foundations:

1. **Open a Discussion first** — Before writing code, let's discuss the theory
2. **Provide evidence** — Empirical data, mathematical proofs, or simulation results
3. **Consider backwards compatibility** — How does this affect existing implementations?
4. **Document thoroughly** — Theory changes need clear explanations

## Code of Conduct

We are committed to providing a welcoming and inclusive environment.

- Be respectful and constructive
- Assume good intent
- Focus on the work, not the person
- Welcome newcomers

Harassment, discrimination, and toxic behavior will not be tolerated.

## Questions?

- Open a GitHub Discussion for general questions
- Email hello@arops.dev for private inquiries
- Join the conversation at [Twin Cities Chaos Engineering Community](https://www.yourlink.com) (update with actual link)

## Recognition

Contributors will be recognized in:
- Release notes
- CONTRIBUTORS.md file
- Project documentation

Thank you for helping build the future of AI resilience engineering.

---

*"The goal is not to prevent failure — it's to make failure visible before it cascades."*
