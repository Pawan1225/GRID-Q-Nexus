from pathlib import Path
import pandas as pd

from src.config import NexusConfig
from src.grid_model.load_cases import load_ieee_case
from src.grid_model.candidates import select_candidate_buses
from src.scenarios.scenario_generator import (
    generate_ai_load_scenarios,
    generate_contingency_scenarios,
)

cfg = NexusConfig()

output_dir = Path("outputs/tables")
output_dir.mkdir(parents=True, exist_ok=True)

summary_rows = []

for case_name in cfg.test_cases:

    print(f"\nLoading {case_name}")

    net = load_ieee_case(case_name)

    candidates = select_candidate_buses(
        net,
        n_bess=cfg.bess_candidate_count,
        n_microgrid=cfg.microgrid_candidate_count,
    )

    ai_loads = generate_ai_load_scenarios(
        net,
        cfg.ai_load_mw_cases,
    )

    contingencies = generate_contingency_scenarios(
        net
    )

    candidates.to_csv(
        output_dir / f"{case_name}_candidate_sites.csv",
        index=False,
    )

    ai_loads.to_csv(
        output_dir / f"{case_name}_ai_load_scenarios.csv",
        index=False,
    )

    contingencies.to_csv(
        output_dir / f"{case_name}_contingencies.csv",
        index=False,
    )

    summary_rows.append(
        {
            "case": case_name,
            "buses": len(net.bus),
            "lines": len(net.line),
            "loads": len(net.load),
            "generators": len(net.gen),
            "candidate_sites": len(candidates),
            "ai_load_scenarios": len(ai_loads),
            "contingencies": len(contingencies),
        }
    )

summary = pd.DataFrame(summary_rows)

summary.to_csv(
    output_dir / "dataset_summary.csv",
    index=False,
)

print("\nDataset Summary")
print(summary)

print("\nPhase 2 setup completed.")