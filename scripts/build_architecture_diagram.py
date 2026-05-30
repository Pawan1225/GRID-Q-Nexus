from pathlib import Path
import matplotlib.pyplot as plt

figs = Path("outputs/figures")
figs.mkdir(parents=True, exist_ok=True)

plt.figure(figsize=(8,10))
plt.axis("off")

steps = [
    "IEEE30 / IEEE118\nGrid Models",
    "Scenario Generator\n(AI Loads + N-1)",
    "AI Candidate Ranking",
    "GRID-Q Search Compression",
    "QUBO Formulation",
    "QAOA / Quantum Layer",
    "Q-RESGRID\nResilience Engine",
    "BESS + Microgrid\nRecommendations"
]

y = 0.95

for step in steps:

    plt.text(
        0.5,
        y,
        step,
        ha="center",
        va="center",
        bbox=dict(boxstyle="round", pad=0.4)
    )

    if y > 0.15:
        plt.arrow(
            0.5,
            y - 0.04,
            0,
            -0.07,
            length_includes_head=True
        )

    y -= 0.11

plt.title(
    "GRID-Q Nexus Architecture",
    fontsize=14,
    pad=20
)

plt.savefig(
    figs / "fig04_architecture.png",
    dpi=300,
    bbox_inches="tight"
)

print("\nSaved:")
print("outputs/figures/fig04_architecture.png")