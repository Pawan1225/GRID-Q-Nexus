# Supplementary Materials

## Overview

This folder contains the complete evidence package supporting the GRID-Q Nexus Phase 2 submissions for:

1. U.S. Department of Energy (DOE)
2. Quantum Computing Inc. (QCi)

The materials provide reproducibility assets, benchmark results, generated scenarios, optimization outputs, and claims-to-evidence mappings used throughout both submissions.

---

# Reproducibility Workflow

Execute the following scripts in sequence:

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

python scripts/build_method_comparison.py

python scripts/build_executive_results.py

python scripts/build_report_assets.py
```

---

# Evidence Files

## Dataset Construction

| File | Description |
|--------|--------|
| dataset_summary.csv | Benchmark network summary |
| ieee30_candidate_sites.csv | IEEE30 candidate locations |
| ieee118_candidate_sites.csv | IEEE118 candidate locations |
| ieee30_ai_load_scenarios.csv | IEEE30 AI load scenarios |
| ieee118_ai_load_scenarios.csv | IEEE118 AI load scenarios |
| ieee30_contingencies.csv | IEEE30 contingency definitions |
| ieee118_contingencies.csv | IEEE118 contingency definitions |

---

## Power Flow Analysis

| File | Description |
|--------|--------|
| power_flow_stress_results.csv | AI-load stress testing results |

---

## BESS Siting

| File | Description |
|--------|--------|
| bess_screening_results.csv | Candidate BESS ranking |
| final_bess_site_ranking.csv | Final BESS rankings |
| final_top3_bess_recommendations.csv | Top recommendations |

---

## Microgrid Resilience

| File | Description |
|--------|--------|
| microgrid_islanding_results.csv | Islanding feasibility evaluation |
| bess_microgrid_resilience_results.csv | BESS-supported resilience improvement |

---

## Quantum Optimization

| File | Description |
|--------|--------|
| qubo_siting_results.csv | QUBO construction and compression |
| qaoa_resource_estimate.csv | Quantum resource estimate |
| classical_vs_hybrid_comparison.csv | Classical vs hybrid comparison |

---

## Submission Assets

| File | Description |
|--------|--------|
| executive_results_table.csv | Executive summary metrics |
| phase2_evidence_summary.csv | Claims-to-evidence mapping |
| final_phase2_recommendation_summary.csv | Final planning recommendations |

---

# Key Figures

Located in:

```text
assets/figures/
```

Files:

```text
fig01_bess_congestion_reduction.png
fig02_resilience_improvement.png
fig03_qubo_compression.png
fig04_architecture.png
```

---

# Benchmark Systems

The prototype uses public benchmark systems:

- IEEE 30-Bus System
- IEEE 118-Bus System

These systems provide reproducible test environments for evaluating energy-storage siting, microgrid planning, resilience analysis, and quantum-ready optimization workflows.

---

# Main Results

| Metric | Result |
|----------|----------|
| Candidate Sites | 20 |
| QUBO Variables | 10 |
| Best Congestion Relief | 136.79 percentage points |
| Resilience Improvement | 0.583 → 0.917 |
| Islanding Feasibility | 33.3% → 66.7% |
| Recommended IEEE30 Sites | 19, 20, 18 |

---

# Notes

All results are generated from publicly reproducible benchmark systems and synthetic planning scenarios.

This repository is intended for research, evaluation, and challenge-submission purposes only.