def pin_control(o):                 # defining a function in this line.
    from machine import Pin         # The function creates a set and then stores a number for each pin.
    po= Pin(o, Pin.OUT)             # If the same number is repeated the 2nd time, the function removes the number
    if o not in a:                  # from the set. The idea is that the number stored in the set will activate
        a.add(o)                    # its respective light.
        po.on()
        print(a)
        print('Pin', o, 'is active.')
        print('Press again to inactive')
    else:
        if o in a:
            po.off()
            a.remove(o)
            print(a)
        print('Pin', o, 'is inactive.')
a=set()
while True:
    o=int(input('Enter pin number: '))
    (pin_control(o))
