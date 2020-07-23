from machine import Pin
a=set()
while True:
    o=int(input('Enter pin number: '))
    
    if o not in a:
        a.add(o)
        po= Pin(o, Pin.OUT)
        po.on()
        print('Pin', o, 'is active.')
        print('Press again to inactive')
    else:         
        if o in a:
            po= Pin(o, Pin.OUT)
            po.off()
            a.remove(o)
        print('Pin', o, 'is inactive.')
    
