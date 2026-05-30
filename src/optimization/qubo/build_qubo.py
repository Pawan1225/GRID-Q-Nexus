import numpy as np


def build_simple_siting_qubo(
    n_variables,
    linear_weights=None,
    penalty_strength=2.0,
    max_selected=None,
):
    """
    Prototype QUBO:
    minimize x^T Q x.

    Negative diagonal weights reward high-value site selection.
    Cardinality penalty controls how many sites are selected.
    """

    if linear_weights is None:
        linear_weights = -np.ones(n_variables)

    Q = np.zeros((n_variables, n_variables))

    for i, w in enumerate(linear_weights):
        Q[i, i] += w

    if max_selected is not None:
        for i in range(n_variables):
            Q[i, i] += penalty_strength * (1 - 2 * max_selected)

            for j in range(i + 1, n_variables):
                Q[i, j] += 2 * penalty_strength

    return Q