from machine import Pin, PWM
from time import sleep

frequency = 5000

led = PWM(Pin(33), frequency)

while True:
    a=int(input("speed: 1-10: "))
    if a not in range (11):
        led.duty(0)
        print('fan off')
        
    else:        
        if a!=10:
            led.duty(a*100)
            sleep(0.005)
        else:
            led.duty(1023)
            sleep(0.005)
        


