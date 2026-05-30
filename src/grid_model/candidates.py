import numpy as np
import pandas as pd


def select_candidate_buses(net, n_bess=20, n_microgrid=10, seed=42):
    rng = np.random.default_rng(seed)

    load_buses = list(net.load.bus.unique()) if len(net.load) else list(net.bus.index)

    bess = rng.choice(load_buses, size=min(n_bess, len(load_buses)), replace=False)
    micro = rng.choice(load_buses, size=min(n_microgrid, len(load_buses)), replace=False)

    all_candidates = sorted(set(bess) | set(micro))

    return pd.DataFrame({
        "bus": [int(b) for b in all_candidates],
        "bess_candidate": [int(b in set(bess)) for b in all_candidates],
        "microgrid_candidate": [int(b in set(micro)) for b in all_candidates],
    })