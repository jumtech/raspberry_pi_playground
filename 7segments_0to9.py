import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
ports = [
  #a, b, c, d, e, f, g,DP
  35,37,38,36,32,33,31,40
]
GPIO.setup(ports, GPIO.OUT)

numbers = [
  #a,b,c,d,e,f,g,p
  [1,1,1,1,1,1,0,0], #0
  [0,1,1,0,0,0,0,0], #1
  [1,1,0,1,1,0,1,0], #2
  [1,1,1,1,0,0,1,0], #3
  [0,1,1,0,0,1,1,0], #4
  [1,0,1,1,0,1,1,0], #5
  [1,0,1,1,1,1,1,0], #6
  [1,1,1,0,0,1,0,0], #7
  [1,1,1,1,1,1,1,0], #8
  [1,1,1,0,0,1,1,0], #9
]

def show_num(no, dot = False):
  ns = numbers[no]
  for i, n in enumerate(ns):
    n = 1 if n == 0 else 0
    GPIO.output(ports[i], n)
  v = GPIO.LOW if dot else GPIO.HIGH
  GPIO.output(ports[7], v)

try:
  for i in range(0,10):
    print(i)
    show_num(i, True)
    sleep(1)

except KeyboardInterrupt:
  pass

GPIO.cleanup()