from adafruit_servokit import ServoKit
import time
import RPi.GPIO as GPIO
from gpiozero import Button
from picamera2 import Picamera2

ledPin = 27
button = Button(17)
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, GPIO.LOW)

while True: 
    if button.is_pressed:
        time.sleep(0.5)
        if button.is_pressed: 
            GPIO.output(ledPin, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(ledPin, GPIO.LOW)
    time.sleep(0.5)

#----------------------------------------

# vexMotor = 18
# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(vexMotor, GPIO.OUT)
# piPWM = GPIO.PWM(vexMotor, 50)	
# piPWM.start(10)

#----------------------------------------

# vibMotor = 27
# GPIO.setup(vibMotor, GPIO.OUT)
# GPIO.output(vibMotor, GPIO.HIGH)


# #initialize servos 
# kit = ServoKit(channels = 16)

# #servo angles that correspond to each bin
# binAngles = [7.5, 22.5, 37.5, 52.5, 67.5, 82.5, 97.5, 112.5, 127.5, 142.5, 157.5, 172.5]

# #set servo angle ranges
# kit.servo[0].actuation_range = 60
# kit.servo[2].actuation_range = 180

# time.sleep(5)

# kit.servo[2].set_pulse_width_range(500, 2500)
# kit.servo[2].angle = 0

# for i in range(0, len(binAngles)):
#     time.sleep(1)
#     kit.servo[2].angle = binAngles[i]