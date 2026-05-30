from pathlib import Path
import numpy as np
import pandas as pd

from src.config import NexusConfig
from src.optimization.qubo.build_qubo import build_simple_siting_qubo

cfg = NexusConfig()
out = Path("outputs/tables")
out.mkdir(parents=True, exist_ok=True)

rows = []

for case_name in cfg.test_cases:
    bess_results = pd.read_csv(out / "bess_screening_results.csv")
    case_bess = bess_results[bess_results["case"] == case_name].copy()

    # Aggregate BESS value by bus.
    bus_scores = (
        case_bess
        .groupby("bess_bus")["congestion_reduction"]
        .mean()
        .fillna(0)
        .sort_values(ascending=False)
    )

    # Keep top sites for quantum-ready subproblem.
    top_sites = bus_scores.head(10)

    if len(top_sites) == 0:
        continue

    values = top_sites.values

    # Higher congestion reduction should be rewarded.
    normalized_values = values / max(abs(values).max(), 1e-9)

    linear_weights = -normalized_values

    Q = build_simple_siting_qubo(
        n_variables=len(top_sites),
        linear_weights=linear_weights,
        penalty_strength=2.0,
        max_selected=3,
    )

    # Brute-force solve small QUBO for prototype validation.
    best_x = None
    best_energy = float("inf")

    for mask in range(2 ** len(top_sites)):
        x = np.array(
            [(mask >> i) & 1 for i in range(len(top_sites))]
        )

        energy = float(x @ Q @ x)

        if energy < best_energy:
            best_energy = energy
            best_x = x

    selected_sites = [
        int(bus)
        for bus, bit in zip(top_sites.index, best_x)
        if bit == 1
    ]

    rows.append({
        "case": case_name,
        "qubo_variables": len(top_sites),
        "raw_candidate_sites": case_bess["bess_bus"].nunique(),
        "selected_bess_sites": selected_sites,
        "selected_count": int(best_x.sum()),
        "best_qubo_energy": best_energy,
        "mean_top_site_value": float(top_sites.mean()),
        "max_top_site_value": float(top_sites.max()),
    })

results = pd.DataFrame(rows)

results.to_csv(
    out / "qubo_siting_results.csv",
    index=False,
)

print("\nQUBO siting results")
print(results)

print("\nSaved: outputs/tables/qubo_siting_results.csv")