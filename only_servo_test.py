import pigpio, time

PIN = 18
MIN_US = 500
MAX_US = 2500

pi = pigpio.pi()
if not pi.connected:
    raise SystemExit("pigpiod is not working!!")

def angle(deg):
    if deg < 0: deg = 0
    if deg > 180: deg = 180
    us = int(MIN_US + (deg/180.0)*(MAX_US - MIN_US))
    pi.set_servo_pulsewidth(PIN, us)

try:
    while True:
        angle(180); time.sleep(2)
        angle(0);   time.sleep(2)
except KeyboardInterrupt:
    pass
finally:
    pi.set_servo_pulsewidth(PIN, 0)
    pi.stop()
