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
            for local_generation_mw in [10, 25, 50]:
                for bess_power_mw in [0, 25, 50, 100]:

                    result = estimate_islanding_feasibility(
                        local_generation_mw=local_generation_mw,
                        bess_power_mw=bess_power_mw,
                        critical_load_mw=critical_load_mw,
                    )

                    result.update({
                        "case": case_name,
                        "microgrid_bus": int(cand["bus"]),
                        "local_generation_mw": local_generation_mw,
                        "bess_power_mw": bess_power_mw,
                    })

                    rows.append(result)

results = pd.DataFrame(rows)

results.to_csv(
    out / "microgrid_islanding_results.csv",
    index=False,
)

print("\nMicrogrid islanding summary")
print(
    results.groupby("case")[
        ["islanding_feasible", "resilience_score", "unserved_critical_mw"]
    ].mean()
)

print("\nTop islanding configurations")
print(
    results.sort_values(
        ["resilience_score", "unserved_critical_mw"],
        ascending=[False, True],
    )
    .head(20)[
        [
            "case",
            "microgrid_bus",
            "critical_load_mw",
            "local_generation_mw",
            "bess_power_mw",
            "served_critical_mw",
            "unserved_critical_mw",
            "islanding_feasible",
            "resilience_score",
        ]
    ]
)

print("\nSaved: outputs/tables/microgrid_islanding_results.csv")