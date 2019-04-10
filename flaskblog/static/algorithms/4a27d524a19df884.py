from PIL import Image
import PIL.ImageOps
import sys   
import os

filepath = sys.argv[1]
filename = sys.argv[2]
image = Image.open(filepath).convert('LA')
image.save(filename)
