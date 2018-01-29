import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
ports = [
  #a, b, c, d, e, f, g,DP
  35,37,38,36,32,33,31,40
]
GPIO.setup(ports, GPIO.OUT)

chars = {
       #a,b,c,d,e,f,g,p
  "P": [1,1,0,0,1,1,1,0],
  "L": [0,0,0,1,1,1,0,0],
  "A": [1,1,1,0,1,1,1,0],
  "I": [0,1,1,0,0,0,0,0],
  "D": [0,1,1,1,1,0,1,0],
}

def show_char(char, dot = False):
  ns = chars[char]
  for i, n in enumerate(ns):
    n = 1 if n == 0 else 0
    GPIO.output(ports[i], n)
  v = GPIO.LOW if dot else GPIO.HIGH
  GPIO.output(ports[7], v)

try:
  plaid = ["P","L","A","I","D"]
  for char in plaid:
    print(char)
    show_char(char, False)
    sleep(1)

except KeyboardInterrupt:
  pass

GPIO.cleanup()