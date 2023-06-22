# Python function that creates a a true random number generator

from sense_hat import SenseHat
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute
import numpy as np

hat = SenseHat()

X = [255, 0, 255]  # Magenta


# Define the execute function that is called by the main controller.
def rand_execute(backend,back):
    n = 6
    sh = 1
    # Create a Quantum Circuit with 16 qubits and 16 bits
    q = QuantumRegister(n,'q')
    c = ClassicalRegister(n,'c')
    circuit = QuantumCircuit(q,c)
    circuit.h(q) # Applies hadamard gate to all qubits
    circuit.measure(q,c) # Measures all qubits  

    # Create a Quantum Program for execution of the circuit on the selected backend
    job = execute(circuit, backend, shots=1)
    # Get the result of the execution and convert to decimal
    result = job.result()
    counts = result.get_counts(circuit)
    binary = list(counts.keys())
    decimal = int(binary[0],2)
    
    hat.show_message(str(decimal), text_colour=X)

