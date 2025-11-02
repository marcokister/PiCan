# this is only a simple way to understand function better!!! better use pigpio it is the gold standard for a servo... 

import RPi.GPIO as GPIO
import time

PIN = 18  # GPIO18 (Pin 12)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

pwm = GPIO.PWM(PIN, 50)  # 50 Hz
pwm.start(0)

MIN_DUTY = 5.0   # ~1.00 ms
MAX_DUTY = 10.0  # ~2.00 ms

def set_angle(deg):
    duty = 2.5 + (deg / 18.0)  # map 0..180 -> 2.5..12.5
    pwm.ChangeDutyCycle(duty)

try:
    while True:
        set_angle(180)
        time.sleep(2)
        set_angle(0)
        time.sleep(2)
except KeyboardInterrupt:
    pass
finally:
    pwm.stop()
    GPIO.cleanup()
