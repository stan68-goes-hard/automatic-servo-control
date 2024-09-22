import RPi.GPIO as GPIO
import time
import numpy as np

# Set up GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)    # Servo 1    ???
GPIO.setup(13, GPIO.OUT)    # Servo 2    ???
servo1 = GPIO.PWM(11, 50)    # pin 11 for servo1 ???
servo2 = GPIO.PWM(13, 50)    # pin 13 for servo2 ???

servo1.start(0)

try:
    servo1.ChangeDutyCycle(2)
    time.sleep(1)
    servo1.ChangeDutyCycle(4)
    time.sleep(1)
    servo1.ChangeDutyCycle(6)
    time.sleep(1)
    servo1.ChangeDutyCycle(8)
    time.sleep(1)
    servo1.ChangeDutyCycle(10)
    time.sleep(1)
    servo1.ChangeDutyCycle(12)
    time.sleep(1)

finally:
    servo1.stop()
    GPIO.cleanup()