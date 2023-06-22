from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, IBMQ, Aer
from sense_hat import SenseHat
hat = SenseHat()

# Colors
blue = (0, 0, 255)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)
purple = (255, 0, 255)
light_blue = (173, 216, 230)
red = (255, 0, 0)
green = (0, 255, 0)

# Define the execute function that is called by the main controller.
def rand_num(backend, back):
    n = 2
    sh = 1
    # Create a Quantum Circuit with 2 qubits and 2 bits
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
    return decimal

def art_execute(backend, back):
    # Create circuit with bell state
    num = rand_num(backend, back)

    n = 4
    
    q = QuantumRegister(n, 'q')
    c = ClassicalRegister(n, 'c')
    circuit1 = QuantumCircuit(q, c)

    circuit1.h(q[0])
    circuit1.h(q[1])
    circuit1.h(q[2])
    circuit1.h(q[3])


    if num == 0:
        circuit1.cx(q[0], q[2])
    elif num == 1:
        circuit1.cx(q[1], q[3])
    elif num == 2:
        circuit1.cx(q[2], q[3])
    elif num == 3:
        circuit1.cx(q[0], q[3])

    circuit1.measure(q,c) # Measures all qubits  
    # Create a Quantum Program for execution of the circuit on the selected backend
    job = execute(circuit1, backend, shots=1)
    # Get the result of the execution and convert to decimal
    result = job.result()
    counts = result.get_counts(circuit1)
    binary = list(counts.keys())
    print(binary)

    # Create circuit with GHZ state
    rand_num2 = rand_num(backend, back)
    n = 4

    # Create circuit
    q = QuantumRegister(n, 'q')
    c = ClassicalRegister(n, 'c')
    circuit2 = QuantumCircuit(q, c)

    circuit2.h(q[0])
    circuit2.h(q[1])
    circuit2.h(q[2])
    circuit2.h(q[3])


    if rand_num2 == 0:
        circuit2.cx(q[0], q[2])
        circuit2.cx(q[0], q[3])
    elif rand_num2 == 1:
        circuit2.cx(q[1], q[3])
        circuit2.cx(q[1], q[2])
    elif rand_num2 == 2:
        circuit2.cx(q[2], q[3])
        circuit2.cx(q[2], q[0])
    elif rand_num2 == 3:
        circuit2.cx(q[0], q[3])
        circuit2.cx(q[0], q[1])

    circuit2.measure(q,c) # Measures all qubits  
    # Create a Quantum Program for execution of the circuit on the selected backend
    job = execute(circuit2, backend, shots=1)
    # Get the result of the execution and convert to decimal
    result = job.result()
    counts = result.get_counts(circuit2)
    binary2 = list(counts.keys())

    # 1*1 square
    rows, cols = (4, 4)
    bin = str(binary)[2:-2]
    arr = [[0 for i in range(cols)] for j in range(rows)]
    for i in range(4):
        for j in range(4): 
            arr[i][j] = bin[i] + bin[j]
            if arr[i][j] == '00':
                hat.set_pixel(i,j+4, green)
            elif arr[i][j] == '01':
                hat.set_pixel(i,j+4, pink)
            elif arr[i][j] == '10':
                hat.set_pixel(i,j+4, red)
            elif arr[i][j] == '11':
                hat.set_pixel(i,j+4, blue)            

    # 1*2 square
    rows, cols = (4, 4)
    bin = str(binary)[2:-2]
    bin2 = str(binary2)[2:-2]
    arr = [[0 for i in range(cols)] for j in range(rows)]
    for i in range(4):
        for j in range(4): 
            arr[i][j] = bin[i] + bin2[j]
            if arr[i][j] == '00':
                hat.set_pixel(i+4,j+4, green)
            elif arr[i][j] == '01':
                hat.set_pixel(i+4,j+4, pink)
            elif arr[i][j] == '10':
                hat.set_pixel(i+4,j+4, red)
            elif arr[i][j] == '11':
                hat.set_pixel(i+4,j+4, blue)  

    # 2*1 square
    rows, cols = (4, 4)
    bin = str(binary)[2:-2]
    bin2 = str(binary2)[2:-2]
    arr = [[0 for i in range(cols)] for j in range(rows)]
    for i in range(4):
        for j in range(4): 
            arr[i][j] = bin2[i] + bin[j]
            if arr[i][j] == '00':
                hat.set_pixel(i,j, green)
            elif arr[i][j] == '01':
                hat.set_pixel(i,j, pink)
            elif arr[i][j] == '10':
                hat.set_pixel(i,j, red)
            elif arr[i][j] == '11':
                hat.set_pixel(i,j, blue)  

    # 2*2 square

    rows, cols = (4, 4)
    bin = str(binary)[2:-2]
    bin2 = str(binary2)[2:-2]
    arr = [[0 for i in range(cols)] for j in range(rows)]
    for i in range(4):
        for j in range(4): 
            arr[i][j] = bin2[i] + bin2[j]
            if arr[i][j] == '00':
                hat.set_pixel(i+4,j, green)
            elif arr[i][j] == '01':
                hat.set_pixel(i+4,j, pink)
            elif arr[i][j] == '10':
                hat.set_pixel(i+4,j, red)
            elif arr[i][j] == '11':
                hat.set_pixel(i+4,j, blue)  

  
