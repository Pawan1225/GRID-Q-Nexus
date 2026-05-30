from pathlib import Path
import ast
import pandas as pd

out = Path("outputs/tables")
qubo_results = pd.read_csv(out / "qubo_siting_results.csv")

rows = []

for _, row in qubo_results.iterrows():
    case_name = row["case"]
    selected_sites = ast.literal_eval(row["selected_bess_sites"])

    # Phase 2 quantum-prototype proxy:
    # We record the QUBO as quantum-ready and estimate QAOA resource needs.
    qubits = int(row["qubo_variables"])
    depth_p1 = 2 * qubits
    depth_p2 = 4 * qubits
    shots = 1024

    rows.append({
        "case": case_name,
        "quantum_method": "QAOA-ready QUBO",
        "qubo_variables": qubits,
        "selected_bess_sites": selected_sites,
        "qaoa_p1_depth_estimate": depth_p1,
        "qaoa_p2_depth_estimate": depth_p2,
        "shots": shots,
        "platform_phase2": "Qiskit simulator / qBraid QIR simulator",
        "platform_phase3": "IBM Heron, IonQ Aria, NVIDIA GPU simulator, or QCi Dirac-3 Hamiltonian mapping",
    })

results = pd.DataFrame(rows)
results.to_csv(out / "qaoa_resource_estimate.csv", index=False)

print("\nQAOA resource estimate")
print(results)

print("\nSaved: outputs/tables/qaoa_resource_estimate.csv")