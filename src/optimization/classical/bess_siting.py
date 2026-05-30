import pandapower as pp


def install_bess(
    net,
    bus,
    power_mw=50,
    energy_mwh=100,
):
    """
    Prototype BESS model.

    Represented as a controllable generator.
    """

    pp.create_sgen(
        net,
        bus=bus,
        p_mw=power_mw,
        q_mvar=0,
        name=f"BESS_{bus}",
    )

    return net