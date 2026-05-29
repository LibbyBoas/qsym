# Source: https://quantumcomputinguk.org/tutorials/introduction-to-bell-states

from qiskit import QuantumCircuit, transpile, ClassicalRegister, QuantumRegister
from qiskit_aer import AerSimulator
from qiskit.circuit.library import QFTGate

backend = AerSimulator() # Using local Aer simulator 

q = QuantumRegister(2,'q')
c = ClassicalRegister(2,'c')

def firstBellState():
    # requires { q[0, 2) : nor ↦ ⊗ i ∈ [0, 2) . ∣0⟩ }
    # ensures { c[0] == c[1] && (c[0] == 1 || c[0] == 0) }
    circuit = QuantumCircuit(q,c)
   
    circuit.h(q[0]) # Hadamard gate 
    #assert { q[0] : had ↦ ∑ k ∈ [0, 2) . 1/sqrt(2) ∣k⟩}
    circuit.cx(q[0],q[1]) # CNOT gate
    # assert { q[0, 2) : en ↦ ∑ j [0, 2) . 1/sqrt(2) . ⊗ i ∈ [0, 2) . ∣j⟩ }
    circuit.measure(q,c) # Qubit Measurment

    print(circuit)

    circuit = transpile(circuit, backend) # Rewrites the circuit to match the backend's basis gates and coupling map
    result = backend.run(circuit,shots=1024).result()
    counts = result.get_counts(circuit)

    print(counts)

print("Creating first Bell State:\n")
firstBellState()
