#Code Import Libery
import time
import RPi.GPIO as GPIO
import LCD1602
#Code
GPIO.setwarnings(False)
#Configure Gpio Pin Number
def setup():
	#Setting GPIO
	LCD1602.init(0x27, 1)

def analog_read(channel):
	r = spi.xfer2([4 | 2 | (channel>>2), (channel & 3) << 6,0])
	acd_out = ((r[1]&15) << 8) + r[2]
	return acd_out

def loop():
	while True:
		pass
		#Code

		#Gas
		gasValue =  analog_read(0)
		print 'Current Gas Level is %i' %gasValue
		if gasValue > 120:
			# > 120
			print 'Gas detected'
			result = 'Gas detected'
		else:
			# < 120
			print  'Not detected'
			result = 'Not detected'
		#LCD1602 
		LCD1602.write(0, 0, gasValue)
		LCD1602.write(1, 1, result)
		#Time to refresh
		time.sleep(1) 
def destroy():
	#Code
	GPIO.cleanup()
	
if __name__ == '__main__':
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()
