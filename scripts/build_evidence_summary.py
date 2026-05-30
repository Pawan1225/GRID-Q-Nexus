from pathlib import Path
import pandas as pd

out = Path("outputs/tables")

dataset = pd.read_csv(out / "dataset_summary.csv")
stress = pd.read_csv(out / "power_flow_stress_results.csv")
bess = pd.read_csv(out / "bess_screening_results.csv")
resilience = pd.read_csv(out / "bess_microgrid_resilience_results.csv")
qubo = pd.read_csv(out / "qubo_siting_results.csv")
qaoa = pd.read_csv(out / "qaoa_resource_estimate.csv")

rows = []

rows.append({
    "evidence_area": "Dataset construction",
    "result": f"{len(dataset)} benchmarks: IEEE30 and IEEE118",
    "source_file": "dataset_summary.csv",
})

worst_stress = stress.sort_values(
    "max_line_loading_percent",
    ascending=False,
    na_position="last",
).iloc[0]

rows.append({
    "evidence_area": "AI load stress impact",
    "result": (
        f"Worst successful stress case: {worst_stress['scenario']} "
        f"with max loading {worst_stress['max_line_loading_percent']:.2f}%"
    ),
    "source_file": "power_flow_stress_results.csv",
})

best_bess = bess.sort_values(
    "congestion_reduction",
    ascending=False,
    na_position="last",
).iloc[0]

rows.append({
    "evidence_area": "BESS siting benefit",
    "result": (
        f"BESS at bus {int(best_bess['bess_bus'])} reduced congestion by "
        f"{best_bess['congestion_reduction']:.2f} percentage points "
        f"for {best_bess['scenario']}"
    ),
    "source_file": "bess_screening_results.csv",
})

res_summary = resilience.groupby("case")[
    ["no_bess_resilience", "with_bess_resilience", "no_bess_feasible", "with_bess_feasible"]
].mean().reset_index()

for _, row in res_summary.iterrows():
    rows.append({
        "evidence_area": f"Microgrid resilience benefit ({row['case']})",
        "result": (
            f"Resilience improved from {row['no_bess_resilience']:.4f} "
            f"to {row['with_bess_resilience']:.4f}; islanding feasibility improved "
            f"from {row['no_bess_feasible']:.4f} to {row['with_bess_feasible']:.4f}"
        ),
        "source_file": "bess_microgrid_resilience_results.csv",
    })

for _, row in qubo.iterrows():
    rows.append({
        "evidence_area": f"QUBO formulation ({row['case']})",
        "result": (
            f"{int(row['raw_candidate_sites'])} raw sites compressed to "
            f"{int(row['qubo_variables'])} QUBO variables; best energy "
            f"{row['best_qubo_energy']:.4f}"
        ),
        "source_file": "qubo_siting_results.csv",
    })

for _, row in qaoa.iterrows():
    rows.append({
        "evidence_area": f"Quantum resource plan ({row['case']})",
        "result": (
            f"{int(row['qubo_variables'])} qubits, p=1 depth estimate "
            f"{int(row['qaoa_p1_depth_estimate'])}, p=2 depth estimate "
            f"{int(row['qaoa_p2_depth_estimate'])}, {int(row['shots'])} shots"
        ),
        "source_file": "qaoa_resource_estimate.csv",
    })

summary = pd.DataFrame(rows)
summary.to_csv(out / "phase2_evidence_summary.csv", index=False)

print("\nPhase 2 Evidence Summary")
print(summary)

print("\nSaved: outputs/tables/phase2_evidence_summary.csv")