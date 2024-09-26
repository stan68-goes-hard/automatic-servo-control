import from RPi.GPIO as GPIO 

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
print("PINs are reset now")
input("Press Enter to exit...")
exit(0)