from PIL import Image
import numpy as np

re = Image.open("resources/images/Player_Sprites.png").convert("RGBA")



for x in range(re.size[0]):
    for y in range(re.size[1]):
        pixel = re.getpixel((x, y))
        if pixel == (64, 192, 64, 255):
            re.putpixel((x, y), (0, 0, 0, 0))

re.show()

