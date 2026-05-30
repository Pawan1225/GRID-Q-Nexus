def greedy_select_candidates(candidate_df, budget_count=10):
    """
    Simple baseline planner:
    prioritize buses that can support both BESS and microgrid placement.
    """

    df = candidate_df.copy()

    df["score"] = (
        df["bess_candidate"] * 1.0
        + df["microgrid_candidate"] * 1.2
    )

    selected = df.sort_values("score", ascending=False).head(budget_count)

    return selected