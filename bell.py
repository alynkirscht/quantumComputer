# -*- coding: utf-8 -*-
# Python function that creates a simple, two qubit quantum cirquit and sets up and measures a Bell, or entangled, state.

# Start by importing and simplifying required modules. 
from sense_hat import SenseHat
hat = SenseHat()

# Define the execute function that is called by the main controller.
def bell_execute(backend,back):
    from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
    from qiskit import execute
    import numpy as np
    #Set number of bits and number of shots
    n = 2
    print(n)
    sh = 1024
    # Create circuit
    qr = QuantumRegister(n)
    cr = ClassicalRegister(n)
    circuit = QuantumCircuit(qr, cr)

    # Add gates to the circuit
    circuit.h(qr[0])
    circuit.cx(qr[0], qr[1])
    circuit.measure(qr[0], cr[0])
    circuit.measure(qr[1], cr[1])
  
    job = execute(circuit, backend, shots=sh)
    # Get the result of the execution
    result = job.result()
    # Provide the results
    print ("Results:")
    #print (result)
    Qdictres = result.get_counts(circuit)
    print(Qdictres)
    
    # Import the Raspberry PI SenseHat display function.
    from histogram_maker import SenseDisplay
    # Display the quantum dictionary as a bar graph on the SenseHat 8x8 pixel display by calling the SenseDisplay function.
    SenseDisplay(Qdictres,n,back)
