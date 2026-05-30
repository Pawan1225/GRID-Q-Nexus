from pathlib import Path
import pandas as pd

from src.config import NexusConfig
from src.microgrid.islanding import estimate_islanding_feasibility

cfg = NexusConfig()
out = Path("outputs/tables")
out.mkdir(parents=True, exist_ok=True)

rows = []

for case_name in cfg.test_cases:
    candidates = pd.read_csv(out / f"{case_name}_candidate_sites.csv")
    microgrid_candidates = candidates[candidates["microgrid_candidate"] == 1]

    for _, cand in microgrid_candidates.iterrows():
        for critical_load_mw in [25, 50, 100]:
            local_generation_mw = 25

            no_bess = estimate_islanding_feasibility(
                local_generation_mw=local_generation_mw,
                bess_power_mw=0,
                critical_load_mw=critical_load_mw,
            )

            with_bess = estimate_islanding_feasibility(
                local_generation_mw=local_generation_mw,
                bess_power_mw=50,
                critical_load_mw=critical_load_mw,
            )

            rows.append({
                "case": case_name,
                "microgrid_bus": int(cand["bus"]),
                "critical_load_mw": critical_load_mw,
                "local_generation_mw": local_generation_mw,
                "no_bess_resilience": no_bess["resilience_score"],
                "with_bess_resilience": with_bess["resilience_score"],
                "resilience_gain": (
                    with_bess["resilience_score"]
                    - no_bess["resilience_score"]
                ),
                "no_bess_unserved_mw": no_bess["unserved_critical_mw"],
                "with_bess_unserved_mw": with_bess["unserved_critical_mw"],
                "unserved_reduction_mw": (
                    no_bess["unserved_critical_mw"]
                    - with_bess["unserved_critical_mw"]
                ),
                "no_bess_feasible": no_bess["islanding_feasible"],
                "with_bess_feasible": with_bess["islanding_feasible"],
            })

results = pd.DataFrame(rows)

results.to_csv(
    out / "bess_microgrid_resilience_results.csv",
    index=False,
)

print("\nBESS + Microgrid resilience summary")
print(
    results.groupby("case")[
        [
            "no_bess_resilience",
            "with_bess_resilience",
            "resilience_gain",
            "no_bess_unserved_mw",
            "with_bess_unserved_mw",
            "unserved_reduction_mw",
            "no_bess_feasible",
            "with_bess_feasible",
        ]
    ].mean()
)

print("\nTop resilience gains")
print(
    results.sort_values(
        ["resilience_gain", "unserved_reduction_mw"],
        ascending=[False, False],
    )
    .head(20)
)

print("\nSaved: outputs/tables/bess_microgrid_resilience_results.csv")