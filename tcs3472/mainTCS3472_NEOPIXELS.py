from tcs34725 import *
from neopixel import NeoPixel

from machine import Pin, I2C
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=100000)

pin = Pin(15, Pin.OUT)   # set GPIO to output to drive NeoPixels
np = NeoPixel(pin, 5)   # create NeoPixel driver on GPIO for 5 pixels
#np[0] = (255, 255, 0) # set the first pixel to white
np.write()              # write data to all pixels
r, g, b = np[0]         # get first pixel colour
if i2c.scan() !=[]:
    sensor = TCS34725(i2c)
    sensor.gain(60)
    data = sensor.read(True)
    colors = list(html_rgb(data))
    colors = list(map(int, colors))
    print(colors)
    for i in range(len(colors)):
        print(i)
        if colors[i] >= 255:
            colors[i] = 255  
    print(colors)
    for i in range(5):
        np[i] = (int(colors[0]), int(colors[1]), int(colors[2]))
        np.write()
    
