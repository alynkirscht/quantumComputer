"""
    Using SenseHat 8x8 display to show bar graph of 2 or 3 qubit Qiskit results dictionaries
"""
# Start by importing and simplifying required modules. 
from sense_hat import SenseHat
#from sense_emu import SenseHat
hat = SenseHat()


# Defining the SenseDisplay function.
def SenseDisplay(InputDict,Qbits,back):
    # Create a default Qdict dictionary with all values 0
    global lst
    lst = [bin(x)[2:].rjust(Qbits, '0') for x in range(2**Qbits)]
    values = [0]*pow(2,Qbits)
    Qdict = dict(zip(lst,values))
        
    # Update the dictionary with the actual dictionary values sent to the function.        
    Qdict.update(InputDict)

    # Scale by dividing by 1024 (shots) - For now assuming 1024, which is set by the sh parameter.
    # Defining the display colors.
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    
    hat.clear()
    hat.set_rotation(270)
    
    # Writing to the SenseHat display pixels.
    for key in Qdict:
        y=7-int(key,2) # Cycle through the states 
        for x in range (0,8): # Cycle through the pixels
                val = ((x+1)*128)-Qdict[key] # The difference between the state result and the pixel x position
                if val<0:
                        #If the state result is greater than the pixel, set pixel color red.
                        color=red
                else:
                    if val>0 and val<128:
                        #If the state result is within the pixel, set pixel color gradient.
                        fade = (255-(2*val),0,(2*val))
                        color=fade
                    else:
                        #If the state result is less than the pixel, set pixel color blue.
                        color=blue
                #Set pixel color.
                hat.set_pixel(x, y, color) 


