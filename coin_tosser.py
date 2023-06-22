# Python function that creates a quantum coin tosser
from sense_hat import SenseHat
from qiskit import QuantumCircuit, Aer, IBMQ, QuantumRegister, ClassicalRegister, execute

hat = SenseHat()

X = [255, 0, 255]  # Magenta
R = [255, 0, 0] # Red
P = [255,255,0] #Yellow
O = [0, 0, 0]  # Black
B = [0,0,255] # Blue
W = [255, 255, 255] #White
G = [0, 255, 0] # Green

# Building the initial circuit
def initial_circuit():
    circuit = QuantumRegister(1, 'circuit')
    measure = ClassicalRegister(1, 'result')
    qc = QuantumCircuit(circuit, measure)
    return qc, circuit, measure

def coin_execute(backend,back):
    qc, circuit, measure = initial_circuit()

    # First turn
    hat.show_message("QC", text_colour=X)
    qc.h(circuit[0])

    # Second turn
    hat.show_message("You", text_colour=X)
    
    run_program = True
    while run_program == True:
        joy_event = hat.stick.wait_for_event()
        if len(joy_event) > 0 and joy_event.action=="pressed":
            if joy_event.direction=="up":
                # Flip coin
                hat.show_message("Flip", text_colour=W)
                run_program = False
            else:
                # No flip
                if joy_event.direction=="down":
                    hat.show_message("No flip", text_colour=X)
                    run_program = False
                else:
                    if joy_event.direction=="left":
                        hat.show_message("No flip", text_colour=X)
                        run_program = False
                    else:
                        if joy_event.direction=="right":
                            hat.show_message("No flip", text_colour=X)
                            run_program = False
                        else:
                            if joy_event.direction=="middle":
                                hat.show_message("No flip", text_colour=X)
                                run_program = False
                
                                    


    # Third turn
    hat.show_message("QC", text_colour=X)
    qc.h(circuit[0]) # Remove superposition

    qc.measure(circuit, measure)

    job = execute(qc, backend, shots=8192)
    res = job.result().get_counts()

    # Winner
    if len(res) == 1 and list(res.keys())[0] == '0':
        hat.show_message("QC Wins",text_colour=R)
    if len(res) == 1 and list(res.keys())[0] == '1':
        hat.show_message("You Win", text_colour=G)
    if len(res) == 2:
        hat.show_message("Tie", text_colour=X)
