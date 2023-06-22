"""
    Main controller for Qiskit on Raspberry PI SenseHat
"""
from sense_hat import SenseHat
from urllib.request import urlopen 
import time  
from qiskit import IBMQ, execute # qiskit class
from qiskit import BasicAer as Aer # qiskit class
import Qconfig_IBMQ_experience  as config
from qiskit.providers.ibmq import least_busy # qiskit class
import random_num
import coin_tosser
import bell
import ghz
import art

sense = SenseHat()

# Background icon
X = [255, 0, 255]  # Magenta
Y = [255,192,203] # Pink
P = [255,255,0] #Yellow
O = [0, 0, 0]  # Black
B = [0,0,255] # Blue
W = [255, 255, 255] #White

# Check if online
def internet_on():
    try:
        response = urlopen('https://www.google.com', timeout=10)
        return True
    except:
        return False

print("Getting provider...")
sense.show_message("Getting provider...", text_colour=W)

if not IBMQ.active_account():
    if internet_on():
        IBMQ.save_account(config.APItoken)
        IBMQ.load_account()
        provider = IBMQ.get_provider()
    else:
        sense.show_message("Offline mode",text_colour= W)

# Set default SenseHat configuration.
sense.clear()
sense.low_light = True

IBM_Q_B = [
B, B, B, W, W, B, B, B,
B, B, W, B, B, W, B, B,
B, W, B, B, B, B, W, B,
B, W, B, B, B, B, W, B,
B, W, B, B, B, B, W, B,
B, P, W, B, B, W, B, B,
P, P, P, W, W, B, B, B,
B, P, B, W, W, W, B, B
]

IBM_AER = [
O, O, W, W, W, W, O, O,
O, W, W, O, O, W, W, O,
W, W, W, O, O, W, W, W,
W, W, O, W, W, O, W, W,
W, W, O, O, O, O, W, W,
W, O, W, W, W, W, O, W,
O, W, O, O, O, O, W, O,
O, O, W, W, W, W, O, O
]
         

# Function to set the backend
def set_backend(back):
    global backend
    if back == "ibmq" and internet_on():
        sense.show_message("Getting best backend...", text_colour=W)
        backend = least_busy(provider.backends(n_qubits=5, operational=True, simulator=False))
        sense.show_message(backend.name(), text_colour=W)
        status = backend.status()
        is_operational = status.operational
        jobs_in_queue = status.pending_jobs
        sense.show_message(str(jobs_in_queue), text_colour=W)
        sense.set_pixels(IBM_Q_B)
    else:
        backend = Aer.get_backend('qasm_simulator')
        sense.show_message(backend.name(), text_colour=W)
        sense.set_pixels(IBM_AER)
    print(backend.name)                
    
# Load the Qiskit function files. Showing messages when starting and when done.
sense.show_message("Qiskit", text_colour=W)

# Initialize the backend to AER
back = "aer" 
set_backend(back)


# The main loop.
# Use the joystick to select and execute one of the Qiskit function files.

while True:
    joy_event = sense.stick.get_events()
    if len(joy_event) > 0 and joy_event[0][2]=="pressed":
        # 2 qubit bell state (entanglement)
        if joy_event[0][1]=="up":
            sense.show_message("Bell", text_colour=B)
            bell.bell_execute(backend,back)
        else:
            # 3 qubit GHZ state  (entanglement)
            if joy_event[0][1]=="down":
                sense.show_message("GHZ", text_colour=B)
                ghz.ghz_execute(backend,back)
            else:
                # Coin tosser
                if joy_event[0][1]=="left":
                    sense.show_message("Coin", text_colour=B)
                    coin_tosser.coin_execute(backend,back)
                else:
                    # Random number generator
                    if joy_event[0][1]=="right":
                        sense.show_message("Random", text_colour=B)
                        random_num.rand_execute(backend,back)
                        
                    else:
                        # Choose Quantum Art
                        if joy_event[0][1]=="middle":
                            sense.show_message("Art", text_colour=B)
                            art.art_execute(backend,back)
                                    


