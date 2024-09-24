import gpiozero as GPIO
import time
import numpy as np
from gpiozero import Servo as servo1

# Set up GPIO
# (check if the pinout is correct)

servo1 = servo1(4) # set up servo on GPIO pin 4

try:
    servo1.min() # set to minimum position
    time.sleep(1)
    servo1.mid() # set to middle position
    time.sleep(1)
    servo1.max() # set to maximum position
    time.sleep(1)
    servo1.value = 0 # set to minimum position
    time.sleep(1)
    servo1.value = 0.5 # set to middle position
    time.sleep(1)
    servo1.value = 1 # set to maximum position
    time.sleep(1)
    servo1.value = 0.5 # set to middle position
    time.sleep(1)
    servo1.value = 0 # set to minimum position
    time.sleep(1)
    servo1.value = -0.5     # set to middle position
    time.sleep(1)
    servo1.value = -1 # set to maximum position
    time.sleep(1)
    servo1.value = -0.5 # set to middle position
    time.sleep(1)
    servo1.value = 0 # set to minimum position
    time.sleep(1)

finally:
   print("Cleaning up")