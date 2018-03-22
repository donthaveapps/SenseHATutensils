from sense_hat import SenseHat
from time import sleep
from random import randint
from evdev import InputDevice, ecodes,list_devices
from select import select 

sense = SenseHat()
sense.set_rotation(180)

# Define colours
# humidity = sense.get_humidity()

if sense.get_humidity() < 30:
    r = (255, 0, 0)
elif sense.get_humidity() < 80:
    r = (0, 100, 0)
else:
    r = (0, 0, 255)
    
o = (255, 127, 0)
y = (255, 255, 0)
G = (0, 255, 0)
b = (0, 0, 255)
i = (75, 0, 130)
v = (159, 0, 255)
w = (240, 240, 240)
g = (50, 50, 50)
e = (0, 0, 0)  # e stands for empty/black

# Define message  text
message1 = "Hello, my name is Inigo Montoya."
text1 = "J"

# Define image

"""
frame0 = [
    w,e,e,e,w,e,e,e,
    w,w,w,w,w,e,e,w,
    w,w,w,w,w,e,e,w,
    w,w,w,w,w,e,e,w,
    e,w,w,w,g,g,w,w,
    e,r,y,r,w,w,w,w,
    e,w,e,w,e,w,e,w,
    e,w,e,w,e,w,e,w
    ]
"""
    
frame1 = [    
    g,e,e,e,g,e,e,e,
    g,g,w,g,g,e,e,g,
    g,w,w,w,g,e,e,g,
    w,w,w,w,w,e,e,w,
    e,w,w,w,g,g,g,w,
    e,r,y,r,w,w,w,w,
    e,g,e,g,e,g,e,g,
    w,e,e,w,e,w,w,e
    ]

frame2 = [
    g,e,e,e,g,e,e,e,
    g,g,w,g,g,e,g,e,
    g,w,w,w,g,e,e,g,
    w,w,w,w,w,e,e,w,
    e,w,w,w,g,g,g,w,
    e,r,y,r,w,w,w,w,
    e,g,e,g,e,g,e,g,
    e,w,w,e,w,e,e,w
    ]

sequence = [frame1, frame2]

# Display message
speed = 0.05

#msg = "{}".format(collar)
#sense.show_message(msg)

while True:
    for i in sequence:
        sense.set_pixels(i)
        sleep(0.7)
        
#    sense.show_message("hello", speed, y, b)
#   sense.show_letter("J", r, b)
#    sleep(0.3)
#    sense.show_letter("J", r)
#    sleep(0.3)
    

# Control
devices = [InputDevice(fn) for fn in list_devices()]
for dev in devices:
    if dev.name == "Raspberry Pi Sense HAT Joystick":
        js = dev
        
while True:
    ro, w, x = select([dev.fd], [], [],0.01)
    for fd in ro:
        for event in dev.read():
            if event.type == ecodes.EV_KEY:# and event.value == 1:
                if event.code == ecodes.KEY_UP:
                    print("up")
                elif event.code == ecodes.KEY_LEFT:
                    print("left")
                elif event.code == ecodes.KEY_RIGHT:
                    print("right")
                elif event.code == ecodes.KEY_DOWN:
                    print("down")
                else:
                    print("enter") 
