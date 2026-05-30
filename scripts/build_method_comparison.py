from pathlib import Path
import pandas as pd

out = Path("outputs/tables")
out.mkdir(parents=True, exist_ok=True)

ranking = pd.read_csv(out / "final_bess_site_ranking.csv")
summary = pd.read_csv(out / "final_phase2_recommendation_summary.csv")
qubo = pd.read_csv(out / "qubo_siting_results.csv")

rows = []

for case_name in ranking["case"].unique():
    case_rank = ranking[ranking["case"] == case_name].copy()
    case_summary = summary[summary["case"] == case_name].iloc[0]
    case_qubo = qubo[qubo["case"] == case_name].iloc[0]

    greedy = case_rank.head(3)

    rows.append({
        "case": case_name,
        "method": "Greedy physical screening",
        "candidate_variables": int(case_qubo["raw_candidate_sites"]),
        "selected_sites": list(greedy["bess_bus"].astype(int)),
        "mean_congestion_reduction": greedy["mean_congestion_reduction"].mean(),
        "max_congestion_reduction": greedy["max_congestion_reduction"].max(),
        "resilience_score": case_summary["with_bess_resilience"],
        "islanding_feasibility": case_summary["with_bess_feasible"],
        "notes": "Classical baseline using ranked congestion benefit",
    })

    rows.append({
        "case": case_name,
        "method": "Hybrid GRID-Q Nexus QUBO/QAOA-ready",
        "candidate_variables": int(case_qubo["qubo_variables"]),
        "selected_sites": case_summary["recommended_bess_buses"],
        "mean_congestion_reduction": case_summary["mean_congestion_reduction"],
        "max_congestion_reduction": case_summary["max_congestion_reduction"],
        "resilience_score": case_summary["with_bess_resilience"],
        "islanding_feasibility": case_summary["with_bess_feasible"],
        "notes": "AI-compressed QUBO subproblem with quantum-ready resource plan",
    })

comparison = pd.DataFrame(rows)

comparison.to_csv(
    out / "classical_vs_hybrid_comparison.csv",
    index=False,
)

print("\nClassical vs Hybrid Comparison")
print(comparison)

print("\nSaved: outputs/tables/classical_vs_hybrid_comparison.csv")