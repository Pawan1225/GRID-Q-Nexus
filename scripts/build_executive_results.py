from pathlib import Path
import pandas as pd

out = Path("outputs/tables")

summary = pd.read_csv(
    out / "final_phase2_recommendation_summary.csv"
)

bess = pd.read_csv(
    out / "bess_screening_results.csv"
)

qubo = pd.read_csv(
    out / "qubo_siting_results.csv"
)

best_bess = (
    bess.sort_values(
        "congestion_reduction",
        ascending=False,
        na_position="last"
    )
    .iloc[0]
)

ieee30 = summary[
    summary["case"] == "ieee30"
].iloc[0]

table = pd.DataFrame({
    "Metric": [
        "Benchmark Networks",
        "AI Data Center Scenarios",
        "N-1 Contingencies",
        "Candidate BESS Sites",
        "QUBO Variables",
        "Best Congestion Reduction",
        "Resilience Improvement",
        "Islanding Feasibility Improvement",
        "Recommended IEEE30 Sites",
    ],
    "Result": [
        "IEEE30, IEEE118",
        "50 MW, 100 MW, 250 MW",
        "10",
        "20",
        "10",
        f"{best_bess['congestion_reduction']:.2f}",
        f"{ieee30['no_bess_resilience']:.3f} -> {ieee30['with_bess_resilience']:.3f}",
        f"{ieee30['no_bess_feasible']:.3f} -> {ieee30['with_bess_feasible']:.3f}",
        ieee30["recommended_bess_buses"],
    ]
})

table.to_csv(
    out / "executive_results_table.csv",
    index=False,
)

print(table)
print("\nSaved: outputs/tables/executive_results_table.csv")