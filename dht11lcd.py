#!/usr/bin/env python
import time
import LCD1602
import Adafruit_DHT
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
pin = 4
sensor = Adafruit_DHT.DHT11

def setup():
        LCD1602.init(0x27, 1)
        GPIO.setmode(GPIO.BCM)

def loop():
        while True:
                pass
                humidity,temperature = Adafruit_DHT.read_retry(sensor,pin)
                if humidity is not None and temperature is not None:
                        print 'Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature,humidity)
                else:
                        print 'Fail'
                temp = 'Temperature = {0:0.1f}*C'.format(temperature)
                humi = 'Humidity = {0:0.1f}%'.format(humidity)
                LCD1602.write(0, 0, temp)
                LCD1602.write(1, 1, humi)
                if temp >= 25:
                        print '>25'
                        GPIO.output(17, GPIO.HIGH)
                else:
                        print 'else'
                        GPIO.output(27, GPIO.HIGH)
                time.sleep(0.5)
                
def destroy():
        GPIO.cleanup()

if __name__ == '__main__':
        setup()
        try:
                loop()
        except KeyboardInterrupt:
                destroy()


