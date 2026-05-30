from pathlib import Path
import pandas as pd
import copy

from src.config import NexusConfig
from src.grid_model.load_cases import load_ieee_case
from src.grid_model.power_flow import (
    run_power_flow,
    add_ai_data_center_load,
    outage_line,
)

cfg = NexusConfig()
out = Path("outputs/tables")
out.mkdir(parents=True, exist_ok=True)

rows = []

for case_name in cfg.test_cases:
    print(f"\nRunning stress tests for {case_name}")

    base_net = load_ieee_case(case_name)

    # Base case
    net = copy.deepcopy(base_net)
    result = run_power_flow(net)
    result.update({
        "case": case_name,
        "scenario": "base_case",
        "ai_load_mw": 0,
        "outage_line": None,
    })
    rows.append(result)

    # AI load cases
    ai_file = out / f"{case_name}_ai_load_scenarios.csv"
    ai_scenarios = pd.read_csv(ai_file)

    for _, row in ai_scenarios.iterrows():
        net = copy.deepcopy(base_net)
        add_ai_data_center_load(
            net,
            bus=int(row["bus"]),
            load_mw=float(row["ai_load_mw"]),
        )

        result = run_power_flow(net)
        result.update({
            "case": case_name,
            "scenario": row["scenario"],
            "ai_load_mw": row["ai_load_mw"],
            "outage_line": None,
        })
        rows.append(result)

    # N-1 line outage cases
    cont_file = out / f"{case_name}_contingencies.csv"
    contingencies = pd.read_csv(cont_file)

    for _, row in contingencies.iterrows():
        net = copy.deepcopy(base_net)
        outage_line(net, int(row["outaged_line"]))

        result = run_power_flow(net)
        result.update({
            "case": case_name,
            "scenario": row["scenario"],
            "ai_load_mw": 0,
            "outage_line": row["outaged_line"],
        })
        rows.append(result)

results = pd.DataFrame(rows)
results.to_csv(out / "power_flow_stress_results.csv", index=False)

print("\nPower-flow stress results")
print(results[[
    "case",
    "scenario",
    "success",
    "total_load_mw",
    "max_line_loading_percent",
    "min_bus_voltage_pu",
]])

print("\nSaved: outputs/tables/power_flow_stress_results.csv")