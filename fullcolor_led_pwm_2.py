import RPi.GPIO as GPIO
import time, sys
import random

PORT_R = 17
PORT_G = 27
PORT_B = 22

GPIO.setmode(GPIO.BCM)
ports = [PORT_R, PORT_G, PORT_B]
for port in ports:
  GPIO.setup(port, GPIO.OUT)

pwm_r = GPIO.PWM(PORT_R, 100000)
pwm_g = GPIO.PWM(PORT_G, 100000)
pwm_b = GPIO.PWM(PORT_B, 100000)

pwm_r.start(0)
pwm_g.start(0)
pwm_b.start(0)

def set_color(r, g, b):
  pwm_r.ChangeDutyCycle(r)
  pwm_g.ChangeDutyCycle(g)
  pwm_b.ChangeDutyCycle(b)

n = r = g = b = 0
try:
  while True:
    r = random.randint(0,100) if n % 3 != 0 else 0
    g = random.randint(0,100) if n % 3 != 1 else 0
    b = random.randint(0,100) if n % 3 != 2 else 0
    n = n + 1 if n < 2 else 0
    print("r: ",r)
    print("g: ",g)
    print("b: ",b)
    print("n: ",n)
    set_color(r, g, b)
    time.sleep(0.1)
except KeyboardInterrupt:
  pass
GPIO.cleanup()
