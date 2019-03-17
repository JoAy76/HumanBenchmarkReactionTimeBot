from PIL import Image, ImageFilter, ImageGrab
from pynput.mouse import Button, Controller
import numpy as np
import sys
import time
import cv2

im=ImageGrab.grab()
mouse = Controller()
sx = 699
sy = 249
ex = 700
ey = 250
def grabImage(filename):
    im=ImageGrab.grab(bbox=(sx, sy, ex, ey))	
    im.save(filename)

def find_rgb(imagename, r_query, g_query, b_query):
    img = Image.open(imagename)
    rgb = img.convert('RGB')
    for x in range(img.size[0]):
       for y in range(img.size[1]):
           r, g, b, = rgb.getpixel((x, y))
           if r == r_query and g == g_query and b == b_query:
               mouse.position = (x + sx, y + sy)
               mouse.click(Button.left, 1)
               return (x, y)
b = 1
while b == 1:
    grabImage('blurred.png')
    print(find_rgb('blurred.png', 47, 134, 208))
    print(find_rgb('blurred.png', 76, 218, 106))
       
    
