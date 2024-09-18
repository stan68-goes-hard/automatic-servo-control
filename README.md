# automatic-servo-control

GPIO needs to be set up(lookup servo control.py):

[Uploading GPIO Servo Control.pimport RPi.GPIO as GPIO
import time
import numpy as np

# Set up GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)    # Servo 1    ???
GPIO.setup(13, GPIO.OUT)    # Servo 2    ???
servo1 = GPIO.PWM(11, 50)    # pin 11 for servo1 ???
servo2 = GPIO.PWM(13, 50)    # pin 13 for servo2 ???


