# GRID-Q Nexus

**Hybrid AI--Quantum Resilient Grid Optimization for Energy Storage, Microgrids, and Contingency Planning**

GRID-Q Nexus is a Phase 2 prototype developed for two Global Industry Challenge 2026 Energy Infrastructure tracks:

1. **U.S. Department of Energy (DOE)**
   - Quantum-Enhanced Strategic Siting of Energy Storage and Microgrids for the Era of AI and Industrial Load Expansion

2. **Quantum Computing Inc. (QCi)**
   - Cost Optimization in Resilient Power Grids

The framework combines power-system simulation, AI-guided search compression, microgrid resilience analysis, QUBO/Hamiltonian formulation, and quantum-ready optimization planning.

---

# Project Lineage

GRID-Q Nexus integrates two prior research modules:

### GRID-Q
Grid expansion planning, congestion analysis, AI-guided candidate filtering, QUBO construction, and quantum-ready optimization.

### Q-RESGRID
Microgrid resilience modeling, islanding feasibility analysis, BESS/DER resource planning, critical-load service evaluation, and contingency assessment.

GRID-Q Nexus combines these capabilities into a unified framework for resilient grid planning.

---

# Key Results

| Metric | Result |
|----------|----------|
| Benchmark Systems | IEEE30, IEEE118 |
| AI Load Scenarios | 50 MW, 100 MW, 250 MW |
| N-1 Contingencies | 10 |
| Candidate Sites | 20 |
| QUBO Variables | 10 |
| Best Congestion Relief | 136.79 percentage points |
| Resilience Improvement | 0.583 → 0.917 |
| Islanding Feasibility | 33.3% → 66.7% |
| Recommended IEEE30 Sites | 19, 20, 18 |

---

# Repository Structure

```text
assets/
  figures/              Final report figures
  tables/               Final report tables

data/
  ieee30/               IEEE30 benchmark assets
  ieee118/              IEEE118 benchmark assets
  ai_loads/             Synthetic AI load scenarios
  contingencies/        Contingency definitions

docs/
  doe/                  DOE submission materials
  qci/                  QCi submission materials
  supplementary/        Evidence package

outputs/
  figures/              Generated figures
  tables/               Generated result tables
  final_assets/         Submission-ready assets

scripts/
  Reproducibility scripts

src/
  grid_model/           Grid simulation
  scenarios/            Scenario generation
  microgrid/            Islanding analysis
  optimization/         Classical and quantum-ready optimization
  evaluation/           Performance metrics
```

---

# Installation

```bash
pip install -r requirements.txt
```

Recommended Python version:

```text
Python 3.10+
```

---

# Reproducing Results

Run the workflow in the following order:

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

Generated outputs will be written to:

```text
outputs/tables/
outputs/figures/
```

---

# Main Evidence Files

| File | Purpose |
|----------|----------|
| dataset_summary.csv | Benchmark network summary |
| power_flow_stress_results.csv | AI load stress evaluation |
| bess_screening_results.csv | BESS siting evaluation |
| microgrid_islanding_results.csv | Islanding feasibility results |
| bess_microgrid_resilience_results.csv | Resilience improvement analysis |
| qubo_siting_results.csv | QUBO compression results |
| qaoa_resource_estimate.csv | Quantum resource estimates |
| phase2_evidence_summary.csv | Claims-to-evidence mapping |
| final_phase2_recommendation_summary.csv | Final recommendations |

---

# DOE Submission Focus

- Strategic BESS siting
- Microgrid planning
- AI-driven load growth
- N-1 contingency analysis
- QUBO optimization
- QAOA-ready planning
- qBraid Phase 3 scaling pathway

---

# QCi Submission Focus

- Microgrid islanding
- DER/BESS resource allocation
- Contingency-response Hamiltonians
- Customer-service continuity
- Critical infrastructure resilience
- Dirac-3 / Entropy Quantum Computing pathway

---

# Reproducibility

The project uses public IEEE benchmark systems and synthetic load-growth scenarios generated programmatically.

All reported results are reproducible using the scripts included in this repository.

---

# Disclaimer

This repository is a research prototype developed for the Global Industry Challenge 2026. Results are intended for research and evaluation purposes only and do not constitute operational planning recommendations.