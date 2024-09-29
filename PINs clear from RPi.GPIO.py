from gpiozero import Servo
from time import sleep

servo = Servo(17)

correction=0.5
maxPW=(2.0+correction)/1000
minPW=(1.0-correction)/1000


servo.mid()
sleep(1)
servo.min()
sleep(1)
servo.max()
sleep(1)
servo.mid()
sleep(1)


servo.close()