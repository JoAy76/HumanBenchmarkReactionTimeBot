from moduleinstaller import *
installModule()
from PIL import Image, ImageFilter
from pynput.mouse import Button, Controller
import pyscreenshot as ImageGrab

im=ImageGrab.grab()
mouse=Controller()


sx = int(input("Start x-coordinate of image grab. Coordinates starts from top left of screen: "))
sy = int(input("Start y-coordinate of image grab. Coordinates starts from top left of screen: "))
ex = int(input("End x-coordinate of image grab. Coordinates starts from top left of screen: "))
ey = int(input("End y-coordinate of image grab. Coordinates starts from top left of screen: "))

filename = input("Filename for image grab (hi.png): ")

r_query = int(input("Red value of pixel: "))
g_query = int(input("Green value of pixel: "))
b_query = int(input("Blue value of pixel: "))

def grabImage(filename):
	im = ImageGrab.grab(bbox = (sx, sy, ex, ey))
	im.save(filename)
def find_rgb(filename, r_query, g_query, b_query):
    img = Image.open(filename)
    rgb = img.convert('RGB')
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            r, g, b, = rgb.getpixel((x, y))
            if r == r_query and g == g_query and b == b_query:
                mouse.position = (x + sx, y + sy)
                mouse.click(Button.left, 1)
    return (x, y)


b = 0
while b == 0:
	grabImage(filename)
	print(find_rgb(filename, r_query, g_query, b_query))

#Version: 3.0.0 Alpha
