# DOE Phase 2 Submission

## Challenge

**Quantum-Enhanced Strategic Siting of Energy Storage and Microgrids for the Era of AI and Industrial Load Expansion**

Global Industry Challenge 2026

---

# Submission Summary

GRID-Q Nexus is a hybrid AI--quantum planning framework for strategic deployment of Battery Energy Storage Systems (BESS) and microgrids under AI-driven load growth and contingency conditions.

The framework combines:

- Grid simulation
- AI-assisted candidate screening
- BESS siting analysis
- Microgrid resilience evaluation
- QUBO optimization
- QAOA-ready quantum formulations
- Planner-facing recommendation generation

---

# Challenge Alignment

The DOE challenge focuses on:

- Energy storage siting
- Microgrid planning
- AI data-center load growth
- Infrastructure resilience
- Quantum optimization

GRID-Q Nexus addresses all five areas through a unified planning workflow.

---

# Internal Module Contributions

## GRID-Q

Provides:

- IEEE network modeling
- Congestion analysis
- Candidate ranking
- Search-space reduction
- QUBO construction

## Q-RESGRID

Provides:

- Microgrid islanding analysis
- Critical-load service evaluation
- Resilience scoring
- Contingency assessment
- BESS support evaluation

---

# Phase 2 Benchmark Configuration

| Metric | Value |
|----------|----------|
| Benchmark Networks | IEEE30, IEEE118 |
| AI Load Scenarios | 50 MW, 100 MW, 250 MW |
| N-1 Contingencies | 10 |
| Candidate Sites | 20 |
| QUBO Variables | 10 |

---

# Key Results

| Metric | Result |
|----------|----------|
| Best Congestion Relief | 136.79 percentage points |
| Resilience Improvement | 0.583 → 0.917 |
| Islanding Feasibility | 33.3% → 66.7% |
| Recommended IEEE30 Sites | 19, 20, 18 |

---

# Main Evidence Files

```text
docs/supplementary/

dataset_summary.csv
power_flow_stress_results.csv
bess_screening_results.csv
microgrid_islanding_results.csv
bess_microgrid_resilience_results.csv
qubo_siting_results.csv
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

# Reproducibility

Run:

```bash
python scripts/run_phase2_setup.py
python scripts/run_power_flow_stress.py
python scripts/run_bess_screening.py
python scripts/run_microgrid_islanding.py
python scripts/run_bess_microgrid_resilience.py
python scripts/run_qubo_siting.py
python scripts/run_qaoa_siting.py
python scripts/build_evidence_summary.py
python scripts/build_final_recommendations.py
```

All reported DOE Phase 2 results can be regenerated using the provided workflow.

---

# Phase 3 Pathway

The proposed Phase 3 implementation targets:

- Larger benchmark systems
- Expanded scenario portfolios
- Joint siting-and-sizing optimization
- qBraid-supported quantum platforms
- Planner-scale deployment studies