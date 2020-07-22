from machine import Pin
from machine import PWM
import time

# Set our pin 2 to PWM
pwm = PWM(Pin(4))

# Frequency = 100hz
pwm.freq(100)


#def pin(i):
while True:
    x= int(input('enter percentage'))
    z=int((x/100)*1023)

    #Brightness between 0 and 1023
    #for brightness in range (0, 1023, 10):
    pwm.duty(z)
    print(z)
'''    time.sleep(0.01)
# Brightness between 1023 and 0
  for brightness in range (1023, 0, -10):
    pwm.duty(brightness)
    print(brightness)
    time.sleep(0.01)
   '''     
