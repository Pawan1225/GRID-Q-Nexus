import pandapower as pp


def run_power_flow(net):
    try:
        pp.runpp(net, numba=False)
        return {
            "success": True,
            "max_line_loading_percent": float(net.res_line.loading_percent.max()),
            "min_bus_voltage_pu": float(net.res_bus.vm_pu.min()),
            "max_bus_voltage_pu": float(net.res_bus.vm_pu.max()),
            "total_load_mw": float(net.load.p_mw.sum()),
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "max_line_loading_percent": None,
            "min_bus_voltage_pu": None,
            "max_bus_voltage_pu": None,
            "total_load_mw": float(net.load.p_mw.sum()),
        }


def add_ai_data_center_load(net, bus, load_mw):
    pp.create_load(
        net,
        bus=bus,
        p_mw=load_mw,
        q_mvar=load_mw * 0.25,
        name=f"AI Data Center {load_mw} MW",
    )
    return net


def outage_line(net, line_id):
    net.line.at[line_id, "in_service"] = False
    return net