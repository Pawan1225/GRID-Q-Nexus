import numpy as np
import pandas as pd


def generate_ai_load_scenarios(net, ai_load_mw_cases=(50, 100, 250), seed=42):
    rng = np.random.default_rng(seed)

    load_buses = list(net.load.bus.unique()) if len(net.load) else list(net.bus.index)
    selected_buses = rng.choice(load_buses, size=min(3, len(load_buses)), replace=False)

    rows = []

    for mw in ai_load_mw_cases:
        for bus in selected_buses:
            rows.append({
                "scenario": f"ai_data_center_{mw}mw_bus_{int(bus)}",
                "bus": int(bus),
                "ai_load_mw": float(mw),
                "type": "ai_load_growth",
            })

    return pd.DataFrame(rows)


def generate_contingency_scenarios(net, max_lines=10, seed=42):
    rng = np.random.default_rng(seed)

    line_ids = list(net.line.index)
    sampled_lines = rng.choice(line_ids, size=min(max_lines, len(line_ids)), replace=False)

    rows = []

    for line in sampled_lines:
        rows.append({
            "scenario": f"n_minus_1_line_{int(line)}",
            "outaged_line": int(line),
            "type": "line_outage",
        })

    return pd.DataFrame(rows)