import RPi.GPIO as GPIO
import time, sys

PORT_R = 17
PORT_G = 27
PORT_B = 22

GPIO.setmode(GPIO.BCM)
ports = [PORT_R, PORT_G, PORT_B]
for port in ports:
  GPIO.setup(port, GPIO.OUT)

pwm_r = GPIO.PWM(PORT_R, 1000)
pwm_g = GPIO.PWM(PORT_G, 1000)
pwm_b = GPIO.PWM(PORT_B, 1000)

pwm_r.start(0)
pwm_g.start(0)
pwm_b.start(0)

def set_color(r, g, b):
  pwm_r.ChangeDutyCycle(r)
  pwm_g.ChangeDutyCycle(g)
  pwm_b.ChangeDutyCycle(b)

r = g = b = 0
try:
  while True:
    if r < 100:
      r += 1
    elif g < 100:
      g += 1
    elif b < 100:
      b += 1
    else:
      r = g = b = 0
    print("r: ",r)
    print("g: ",g)
    print("b: ",b)
    set_color(r, g, b)
    time.sleep(0.1)
except KeyboardInterrupt:
  pass
GPIO.cleanup()
