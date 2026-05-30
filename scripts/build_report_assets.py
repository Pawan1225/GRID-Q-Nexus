from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

out = Path("outputs")
tables = out / "tables"
figs = out / "figures"

figs.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------
# Figure 1
# BESS Congestion Reduction
# --------------------------------------------------

bess = pd.read_csv(tables / "bess_screening_results.csv")

top10 = (
    bess.sort_values(
        "congestion_reduction",
        ascending=False,
        na_position="last",
    )
    .head(10)
)

plt.figure(figsize=(8,5))

plt.bar(
    range(len(top10)),
    top10["congestion_reduction"]
)

plt.xticks(
    range(len(top10)),
    top10["bess_bus"],
    rotation=45
)

plt.ylabel("Congestion Reduction")
plt.xlabel("BESS Bus")
plt.title("Top BESS Siting Candidates")

plt.tight_layout()

plt.savefig(
    figs / "fig01_bess_congestion_reduction.png",
    dpi=300,
)

plt.close()

# --------------------------------------------------
# Figure 2
# Resilience Improvement
# --------------------------------------------------

res = pd.read_csv(
    tables / "bess_microgrid_resilience_results.csv"
)

summary = (
    res.groupby("case")[
        [
            "no_bess_resilience",
            "with_bess_resilience",
        ]
    ]
    .mean()
)

plt.figure(figsize=(6,4))

summary.plot(
    kind="bar"
)

plt.ylabel("Resilience Score")

plt.title(
    "Microgrid Resilience Improvement with BESS"
)

plt.tight_layout()

plt.savefig(
    figs / "fig02_resilience_improvement.png",
    dpi=300,
)

plt.close()

# --------------------------------------------------
# Figure 3
# QUBO Compression
# --------------------------------------------------

qubo = pd.read_csv(
    tables / "qubo_siting_results.csv"
)

plt.figure(figsize=(6,4))

x = range(len(qubo))

plt.bar(
    [i-0.2 for i in x],
    qubo["raw_candidate_sites"],
    width=0.4,
    label="Raw"
)

plt.bar(
    [i+0.2 for i in x],
    qubo["qubo_variables"],
    width=0.4,
    label="QUBO"
)

plt.xticks(
    x,
    qubo["case"]
)

plt.ylabel("Variables")
plt.title("Search Space Compression")

plt.legend()

plt.tight_layout()

plt.savefig(
    figs / "fig03_qubo_compression.png",
    dpi=300,
)

plt.close()

print("\nFigures generated:")
print(figs)