from machine import Pin, PWM
from time import sleep
p1 = Pin(32, Pin.OUT)

frequency = 5000

led = PWM(Pin(33), frequency)

while True:
    a=int(input("speed: 1-10: "))
    if a!=10:
        led.duty(a*100)
        sleep(0.005)
    else:
        led.duty(1023)
        sleep(0.005)



