import time
import RPi.GPIO as GPIO

#Code Setting Warrnings
GPIO.setwarnings(False)
#Code Setting Pin Number
pin = 1
def setup():
	#Code GPIO
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(pin, GPIO.IN)
def loop():
	while True:
		pass
		#Code
		value = GPIO.input(pin)
		print value
		#If -> Else

		#Doing
def destroy():
	#Code
	GPIO.cleanup()
	
if __name__ == '__main__':
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()
