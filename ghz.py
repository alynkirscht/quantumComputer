"""
    Creates a simple, three qubit quantum cirquit and sets up and measures an entangled GHZ state.
    Displays a histogram
"""

from sense_hat import SenseHat
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute

hat = SenseHat()

# Define the execute function that is called by the main controller.
def ghz_execute(backend,back):
    
    #Set number of bits and number of shots
    n = 3
    sh = 1024

    # Create circuit
    qr = QuantumRegister(n)
    cr = ClassicalRegister(n)
    circuit = QuantumCircuit(qr, cr)

    # Add gates to the circuit
    circuit.reset(qr[0])
    circuit.reset(qr[1])
    circuit.reset(qr[2])
    circuit.h(qr[0])
    circuit.cx(qr[0], qr[1])
    circuit.cx(qr[0], qr[2])
    circuit.measure(qr[0], cr[0])
    circuit.measure(qr[1], cr[1])
    circuit.measure(qr[2], cr[2])

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
