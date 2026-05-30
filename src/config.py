from dataclasses import dataclass

@dataclass
class NexusConfig:
    test_cases: tuple = ("ieee30", "ieee118")

    bess_candidate_count: int = 20
    microgrid_candidate_count: int = 10

    ai_load_mw_cases: tuple = (50, 100, 250)
    capacity_levels_mwh: tuple = (0, 50, 100, 250)

    scenarios: tuple = (
        "normal",
        "ai_load_growth",
        "line_outage",
        "generator_outage",
        "weather_derating",
        "microgrid_islanding",
        "combined_stress",
    )

    qaoa_qubits_target: tuple = (10, 16)
    shots: int = 1024
    qaoa_depth: int = 2