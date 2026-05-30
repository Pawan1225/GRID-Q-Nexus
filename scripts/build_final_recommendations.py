from pathlib import Path
import pandas as pd

out = Path("outputs/tables")
out.mkdir(parents=True, exist_ok=True)

bess = pd.read_csv(out / "bess_screening_results.csv")
resilience = pd.read_csv(out / "bess_microgrid_resilience_results.csv")
qubo = pd.read_csv(out / "qubo_siting_results.csv")

# --------------------------------------------------
# 1. BESS site ranking from physical grid benefit
# --------------------------------------------------

site_rank = (
    bess.groupby(["case", "bess_bus"])
    .agg(
        mean_congestion_reduction=("congestion_reduction", "mean"),
        max_congestion_reduction=("congestion_reduction", "max"),
        mean_voltage_after_bess=("bess_min_voltage", "mean"),
        successful_runs=("bess_success", "sum"),
        total_runs=("bess_success", "count"),
    )
    .reset_index()
)

site_rank["success_rate"] = (
    site_rank["successful_runs"] / site_rank["total_runs"]
)

# --------------------------------------------------
# 2. Add simple normalized hybrid score
# --------------------------------------------------

site_rank["score"] = (
    site_rank["mean_congestion_reduction"].fillna(0)
    + 0.25 * site_rank["max_congestion_reduction"].fillna(0)
    + 10.0 * site_rank["success_rate"].fillna(0)
)

site_rank = site_rank.sort_values(
    ["case", "score"],
    ascending=[True, False],
)

site_rank.to_csv(
    out / "final_bess_site_ranking.csv",
    index=False,
)

# --------------------------------------------------
# 3. Top 3 recommended sites per case
# --------------------------------------------------

top3 = (
    site_rank.groupby("case")
    .head(3)
    .reset_index(drop=True)
)

top3.to_csv(
    out / "final_top3_bess_recommendations.csv",
    index=False,
)

# --------------------------------------------------
# 4. Report-level summary
# --------------------------------------------------

summary_rows = []

for case_name, group in top3.groupby("case"):
    buses = list(group["bess_bus"].astype(int))

    summary_rows.append({
        "case": case_name,
        "recommended_bess_buses": buses,
        "mean_congestion_reduction": group["mean_congestion_reduction"].mean(),
        "max_congestion_reduction": group["max_congestion_reduction"].max(),
        "mean_success_rate": group["success_rate"].mean(),
    })

summary = pd.DataFrame(summary_rows)

# Add resilience summary.
res_summary = (
    resilience.groupby("case")
    .agg(
        no_bess_resilience=("no_bess_resilience", "mean"),
        with_bess_resilience=("with_bess_resilience", "mean"),
        no_bess_feasible=("no_bess_feasible", "mean"),
        with_bess_feasible=("with_bess_feasible", "mean"),
        mean_unserved_reduction_mw=("unserved_reduction_mw", "mean"),
    )
    .reset_index()
)

summary = summary.merge(
    res_summary,
    on="case",
    how="left",
)

summary.to_csv(
    out / "final_phase2_recommendation_summary.csv",
    index=False,
)

print("\nFinal Top 3 BESS Recommendations")
print(top3)

print("\nFinal Phase 2 Recommendation Summary")
print(summary)

print("\nSaved:")
print("outputs/tables/final_bess_site_ranking.csv")
print("outputs/tables/final_top3_bess_recommendations.csv")
print("outputs/tables/final_phase2_recommendation_summary.csv")