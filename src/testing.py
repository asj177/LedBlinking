import RPi.GPIO as GPIO
import time

LEDPIN1=13
LEDPIN2=5
LEDPIN3=17
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDPIN1,GPIO.OUT)
GPIO.setup(LEDPIN2,GPIO.OUT)
GPIO.setup(LEDPIN3,GPIO.OUT)

i=0
while i<3:
    GPIO.output(LEDPIN1,True)
    time.sleep(1)
    GPIO.output(LEDPIN1,False)
    GPIO.output(LEDPIN2,True)
    time.sleep(1)
    GPIO.output(LEDPIN2,False)
    GPIO.output(LEDPIN3,True)
    time.sleep(1)
    GPIO.output(LEDPIN3,False)
    i=i+1

GPIO.cleanup()