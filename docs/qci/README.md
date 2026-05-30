# QCi Phase 2 Submission

## Challenge

**Cost Optimization in Resilient Power Grids**

Global Industry Challenge 2026

Quantum Computing Inc. (QCi)

---

# Submission Summary

GRID-Q Nexus is a hybrid quantum-classical framework for resilient microgrid design, islanding optimization, contingency-response planning, and DER/BESS resource allocation.

The framework combines:

- Transmission-grid modeling
- Microgrid identification
- BESS and DER resource planning
- Islanding feasibility analysis
- Hamiltonian formulation
- Contingency evaluation
- Entropy Quantum Computing (EQC) integration

The objective is to maximize customer service continuity and critical infrastructure availability while minimizing resource deployment costs during contingency conditions.

---

# Challenge Alignment

The QCi challenge focuses on:

- Microgrid design
- Islanding feasibility
- Hamiltonian formulation
- DER resource allocation
- Contingency handling
- Entropy Quantum Computing optimization

GRID-Q Nexus addresses each challenge stage through a unified hybrid planning workflow.

---

# Internal Module Contributions

## GRID-Q

Provides:

- Grid topology analysis
- Candidate region identification
- Search-space compression
- QUBO/Hamiltonian construction
- Quantum-ready optimization encoding

## Q-RESGRID

Provides:

- Microgrid design
- Islanding feasibility evaluation
- Critical-load continuity analysis
- DER/BESS support planning
- Resilience scoring

---

# Challenge Stage Mapping

## Stage 1 — Microgrid Design

- Candidate microgrid identification
- BESS reinforcement planning
- DER allocation
- Islanding feasibility assessment

## Stage 2 — Hamiltonian Formulation

Two optimization Hamiltonians are defined:

### Islanding Hamiltonian

Optimizes:

- Customer service continuity
- Critical-load support
- Resource deployment cost

### DER Hamiltonian

Optimizes:

- Local power balance
- DER allocation
- Resource activation cost

## Stage 3 — Contingency Evaluation

Evaluated scenarios include:

- N-1 transmission outages
- PCC failures
- DER failures
- High-load operating conditions

---

# Phase 2 Benchmark Configuration

| Metric | Value |
|----------|----------|
| Benchmark Networks | IEEE30, IEEE118 |
| Candidate Sites | 20 |
| Hamiltonian Variables | 10 |
| Contingency Scenarios | 10 |
| Microgrid Evaluation | Grid-Connected + Islanded |

---

# Key Results

| Metric | Result |
|----------|----------|
| Resilience Improvement | 0.583 → 0.917 |
| Islanding Feasibility | 33.3% → 66.7% |
| Candidate Compression | 20 → 10 |
| Quantum Formulation | Hamiltonian Ready |
| Platform Target | Dirac-3 EQC |

---

# Main Evidence Files

```text
docs/supplementary/

microgrid_islanding_results.csv
bess_microgrid_resilience_results.csv
qubo_siting_results.csv
qaoa_resource_estimate.csv
phase2_evidence_summary.csv
final_phase2_recommendation_summary.csv
```

---

# Figures

```text
assets/figures/

fig01_bess_congestion_reduction.png
fig02_resilience_improvement.png
fig03_qubo_compression.png
fig04_architecture.png
```

---

# Quantum Platform Justification

GRID-Q Nexus is designed for Entropy Quantum Computing workflows.

The proposed Hamiltonians are naturally compatible with:

- Fully connected optimization graphs
- Higher-order polynomial interactions
- Hybrid classical-quantum decomposition

These characteristics align closely with QCi's Dirac-3 architecture.

---

# Reproducibility

Run:

```bash
python scripts/run_phase2_setup.py
python scripts/run_bess_screening.py
python scripts/run_microgrid_islanding.py
python scripts/run_bess_microgrid_resilience.py
python scripts/run_qubo_siting.py
python scripts/run_qaoa_siting.py
python scripts/build_evidence_summary.py
python scripts/build_final_recommendations.py
```

All Phase 2 results can be regenerated from the provided workflow.

---

# Phase 3 Pathway

The proposed Phase 3 implementation targets:

- Dirac-3 Entropy Quantum Computing
- Larger microgrid portfolios
- Expanded contingency sets
- Planner-scale transmission systems
- Quantum-enhanced resilience optimization

The Phase 2 prototype establishes the Hamiltonian foundation required for large-scale contingency-response optimization on QCi infrastructure.