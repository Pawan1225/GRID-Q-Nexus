from pathlib import Path
import copy
import pandas as pd

from src.config import NexusConfig
from src.grid_model.load_cases import load_ieee_case
from src.grid_model.power_flow import (
    run_power_flow,
    add_ai_data_center_load,
)
from src.optimization.classical.bess_siting import install_bess

cfg = NexusConfig()
out = Path("outputs/tables")
out.mkdir(parents=True, exist_ok=True)

rows = []

for case_name in cfg.test_cases:
    print(f"\nRunning BESS screening for {case_name}")

    base_net = load_ieee_case(case_name)

    candidates = pd.read_csv(out / f"{case_name}_candidate_sites.csv")
    bess_candidates = candidates[candidates["bess_candidate"] == 1]

    ai_scenarios = pd.read_csv(out / f"{case_name}_ai_load_scenarios.csv")

    for _, scenario in ai_scenarios.iterrows():

        # stressed baseline
        stressed_net = copy.deepcopy(base_net)
        add_ai_data_center_load(
            stressed_net,
            bus=int(scenario["bus"]),
            load_mw=float(scenario["ai_load_mw"]),
        )

        stressed_result = run_power_flow(stressed_net)

        for _, cand in bess_candidates.iterrows():
            net = copy.deepcopy(base_net)

            add_ai_data_center_load(
                net,
                bus=int(scenario["bus"]),
                load_mw=float(scenario["ai_load_mw"]),
            )

            install_bess(
                net,
                bus=int(cand["bus"]),
                power_mw=50,
                energy_mwh=100,
            )

            result = run_power_flow(net)

            baseline_loading = stressed_result["max_line_loading_percent"]
            bess_loading = result["max_line_loading_percent"]

            if baseline_loading is not None and bess_loading is not None:
                congestion_reduction = baseline_loading - bess_loading
            else:
                congestion_reduction = None

            rows.append({
                "case": case_name,
                "scenario": scenario["scenario"],
                "ai_load_bus": int(scenario["bus"]),
                "ai_load_mw": float(scenario["ai_load_mw"]),
                "bess_bus": int(cand["bus"]),
                "bess_power_mw": 50,
                "bess_energy_mwh": 100,
                "baseline_success": stressed_result["success"],
                "bess_success": result["success"],
                "baseline_max_loading": baseline_loading,
                "bess_max_loading": bess_loading,
                "congestion_reduction": congestion_reduction,
                "baseline_min_voltage": stressed_result["min_bus_voltage_pu"],
                "bess_min_voltage": result["min_bus_voltage_pu"],
            })

results = pd.DataFrame(rows)

results.to_csv(
    out / "bess_screening_results.csv",
    index=False,
)

print("\nTop BESS siting results")
print(
    results.sort_values(
        "congestion_reduction",
        ascending=False,
        na_position="last",
    )
    .head(20)[
        [
            "case",
            "scenario",
            "bess_bus",
            "baseline_max_loading",
            "bess_max_loading",
            "congestion_reduction",
            "baseline_min_voltage",
            "bess_min_voltage",
        ]
    ]
)

print("\nSaved: outputs/tables/bess_screening_results.csv")