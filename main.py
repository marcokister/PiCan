import pigpio
import time
import RPi.GPIO as GPIO


PIN = 18
MIN_US = 500
MAX_US = 2500

TRIG = 23
ECHO = 24
distance = 9.0

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

pi = pigpio.pi()
if not pi.connected:
    raise SystemExit("pigpiod service not running or available")

def angle(deg):
    if deg < 0: deg = 0
    if deg > 180: deg = 180
    us = int(MIN_US + (deg/180.0)*(MAX_US - MIN_US))
    pi.set_servo_pulsewidth(PIN, us)


    
angle(100)

while True:
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()


    pulse_duration = pulse_end - pulse_start
    measured_distance = round(pulse_duration * 17150, 2)
    print(measured_distance, "cm")

    if measured_distance <= distance:
        print("distance sensor activated!")
        angle(40)
        time.sleep(1.8)
        angle(100)

    time.sleep(0.5)
