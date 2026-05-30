import pandapower.networks as pn


def load_ieee_case(case_name: str):
    case_name = case_name.lower()

    if case_name == "ieee30":
        return pn.case30()

    if case_name == "ieee118":
        return pn.case118()

    raise ValueError(f"Unsupported case: {case_name}")