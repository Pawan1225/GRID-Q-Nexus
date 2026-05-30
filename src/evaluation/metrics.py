def resilience_score(load_served_mw, total_critical_load_mw):
    """
    Fraction of critical load successfully served.
    """

    if total_critical_load_mw <= 0:
        return 1.0

    return max(
        0.0,
        min(
            1.0,
            load_served_mw / total_critical_load_mw
        )
    )


def expected_unserved_energy(
    total_demand_mw,
    served_demand_mw,
    hours=1
):
    """
    EUE metric used in grid planning.
    """

    return max(
        0.0,
        total_demand_mw - served_demand_mw
    ) * hours


def critical_load_served_percent(
    served_critical_mw,
    total_critical_mw
):
    """
    Critical load served percentage.
    """

    if total_critical_mw <= 0:
        return 100.0

    return (
        100.0
        * served_critical_mw
        / total_critical_mw
    )


def customer_service_rate(
    customers_served,
    total_customers
):
    """
    QCi metric.
    """

    if total_customers <= 0:
        return 1.0

    return customers_served / total_customers


def outage_hours(
    customers_unserved,
    outage_duration_hours
):
    """
    Customer outage-hours.
    """

    return customers_unserved * outage_duration_hours