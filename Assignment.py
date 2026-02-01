# Assingment 3 
import RPi.GPIO as GPIO
import time

Green = 11 #Pin for green LED
Yellow = 13 #Pin for yellow LED
Red = 15 #Pin for red LED
buttonPin = 16 #Pin for Button

# Setup for the code
def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Green, GPIO.OUT)
    GPIO.setup(Yellow, GPIO.OUT)
    GPIO.setup(Red, GPIO.OUT)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

"""The code will continue to loop depending
when the button is pressed. It will start with the
green light on, wait for 10 sec then turn the yellow light on.
After three sec the yellow light turns off and the red will be switched on
for 5 sec. After 5 sec the green light will be turned on again"""
def loop():
    while True:
        GPIO.output(Green,GPIO.HIGH)
        if GPIO.input(buttonPin)==GPIO.LOW:
            time.sleep(10)
            GPIO.output(Green,GPIO.LOW)
            GPIO.output(Yellow,GPIO.HIGH)
            time.sleep(3)
            GPIO.output(Yellow,GPIO.LOW)
            GPIO.output(Red,GPIO.HIGH)
            time.sleep(20)
            GPIO.output(Yellow,GPIO.HIGH)
            GPIO.output(Red,GPIO.HIGH)
            time.sleep(5)
            GPIO.output(Green,GPIO. HIGH)

        else:
            GPIO.output(Green,GPIO. HIGH)
            GPIO.output(Yellow,GPIO.LOW)
            GPIO.output(Red,GPIO.LOW)

# Destroy function
def destroy():
    GPIO.output(Green,GPIO.LOW)
    GPIO.output(Yellow,GPIO.LOW)
    GPIO.output(Red,GPIO.LOW)
    GPIO.cleanup()

# Start of code
if __name__ == '__main__':
    print ('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
