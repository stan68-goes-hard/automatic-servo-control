import from RPi.GPIO as GPIO 

GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()
print("PINs are reset now")
input("Press Enter to exit...")
if input is True:
exit(0)