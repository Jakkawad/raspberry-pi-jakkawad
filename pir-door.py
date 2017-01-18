import time
import RPi.GPIO as GPIO
GPIO.setmode(BPIO.BCM)
 
pir_pin = 18 #GPIO18
#led_pin = 23 #GPIO23
 
GPIO.setup(pir_pin, GPIO.IN)         # activate input
#GPIO.setup(led_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # activate input with PullUp
 
while True:
    value = GPIO.input(pir_pin)
    if :
        print value
    else:
        print 'Value = nil'
#    if GPIO.input(pir_pin):
#        print("PIR ALARM!")
#    if GPIO.input(led_pin):
#        print("DOOR ALARM!")
    time.sleep(0.5)
