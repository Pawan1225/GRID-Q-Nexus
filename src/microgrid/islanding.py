def estimate_islanding_feasibility(
    local_generation_mw,
    bess_power_mw,
    critical_load_mw,
):
    available_power = local_generation_mw + bess_power_mw

    served_critical_mw = min(
        available_power,
        critical_load_mw,
    )

    unserved_critical_mw = max(
        0.0,
        critical_load_mw - available_power,
    )

    feasibility = available_power >= critical_load_mw

    resilience = (
        served_critical_mw / critical_load_mw
        if critical_load_mw > 0
        else 1.0
    )

    return {
        "available_power_mw": available_power,
        "critical_load_mw": critical_load_mw,
        "served_critical_mw": served_critical_mw,
        "unserved_critical_mw": unserved_critical_mw,
        "islanding_feasible": feasibility,
        "resilience_score": resilience,
    }