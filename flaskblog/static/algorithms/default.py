from PIL import Image
import PIL.ImageOps
import sys   
import os

filepath = sys.argv[1]
filename = sys.argv[2]
image = Image.open(filepath)
inverted_image = PIL.ImageOps.invert(image)
inverted_image.save(filename)