from tcs34725 import *
from neopixel import NeoPixel
from machine import Pin, I2C # hardware i2c on ESP32 

i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=100000)
pin = Pin(15, Pin.OUT)   # set GPIO to output to drive NeoPixels
num_pixels = 5           # numbe of pixels on strip or ring -> 5 pixels
np = NeoPixel(pin, num_pixels)   # create NeoPixel driver on GPIO for 5 pixels

np.write()              # write data to all pixels
r, g, b = np[0]         # get first pixel colour
if i2c.scan() !=[]:   
    sensor = TCS34725(i2c)  # create TCS34725 instance
    sensor.gain(60)   
    data = sensor.read(True)  # read from sensor and store returned data   
    colors = list(html_rgb(data))  # convert returned data from tuple to list   
    colors = list(map(int, colors))  # convert items in list to int values instead of float
    print(colors)  
    for i in range(len(colors)):  # keeps values below 255 
        print(i)
        if colors[i] >= 255:
            colors[i] = 255  
    print(colors)
    for i in range(num_pixels):  # set all pixels to the color detected from tcs3472 color sensor
        np[i] = (int(colors[0]), int(colors[1]), int(colors[2]))
        np.write()
    
