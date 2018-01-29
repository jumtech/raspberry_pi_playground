import RPi.GPIO as GPIO
import time, sys
import random

R1 = 17
G1 = 27
B1 = 22

R2 = 10
G2 = 9
B2 = 11

R3 = 5
G3 = 6
B3 = 13

R4 = 19
G4 = 26
B4 = 21

R5 = 20
G5 = 16
B5 = 12

R6 = 7
G6 = 8
B6 = 25

GPIO.setmode(GPIO.BCM)
ports = [
  R1, G1, B1,
  R2, G2, B2,
  R3, G3, B3,
  R4, G4, B4,
  R5, G5, B5,
  R6, G6, B6,
]
for port in ports:
  GPIO.setup(port, GPIO.OUT)

def pwm_start(pwm_r, pwm_g, pwm_b):
  pwm_r.start(0)
  pwm_g.start(0)
  pwm_b.start(0)

pwm_r1 = GPIO.PWM(R1, 1000)
pwm_g1 = GPIO.PWM(G1, 1000)
pwm_b1 = GPIO.PWM(B1, 1000)
pwm_start(pwm_r1, pwm_g1, pwm_b1)

pwm_r2 = GPIO.PWM(R2, 1000)
pwm_g2 = GPIO.PWM(G2, 1000)
pwm_b2 = GPIO.PWM(B2, 1000)
pwm_start(pwm_r2, pwm_g2, pwm_b2)

pwm_r3 = GPIO.PWM(R3, 1000)
pwm_g3 = GPIO.PWM(G3, 1000)
pwm_b3 = GPIO.PWM(B3, 1000)
pwm_start(pwm_r3, pwm_g3, pwm_b3)

pwm_r4 = GPIO.PWM(R4, 1000)
pwm_g4 = GPIO.PWM(G4, 1000)
pwm_b4 = GPIO.PWM(B4, 1000)
pwm_start(pwm_r4, pwm_g4, pwm_b4)

pwm_r5 = GPIO.PWM(R5, 1000)
pwm_g5 = GPIO.PWM(G5, 1000)
pwm_b5 = GPIO.PWM(B5, 1000)
pwm_start(pwm_r5, pwm_g5, pwm_b5)

pwm_r6 = GPIO.PWM(R6, 1000)
pwm_g6 = GPIO.PWM(G6, 1000)
pwm_b6 = GPIO.PWM(B6, 1000)
pwm_start(pwm_r6, pwm_g6, pwm_b6)

def set_random_color(pwm_r, pwm_g, pwm_b):
  n = random.randint(0,3)
  rgb = [random.randint(0,100), random.randint(0,100), random.randint(0,100)]
  if n != 3:
    rgb[n] = 0
  print("r: ",rgb[0])
  print("g: ",rgb[1])
  print("b: ",rgb[2])
  print("n: ",n)
  pwm_r.ChangeDutyCycle(rgb[0])
  pwm_g.ChangeDutyCycle(rgb[1])
  pwm_b.ChangeDutyCycle(rgb[2])

try:
  while True:
    set_random_color(pwm_r1, pwm_g1, pwm_b1)
    set_random_color(pwm_r2, pwm_g2, pwm_b2)
    set_random_color(pwm_r3, pwm_g3, pwm_b3)
    set_random_color(pwm_r4, pwm_g4, pwm_b4)
    set_random_color(pwm_r5, pwm_g5, pwm_b5)
    set_random_color(pwm_r6, pwm_g6, pwm_b6)
    time.sleep(0.1)
except KeyboardInterrupt:
  pass
GPIO.cleanup()
