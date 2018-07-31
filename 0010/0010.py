# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 13:01:26 2018

@author: zhang
"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy, random, numexpr
path = os.path.split(os.path.realpath(__file__))[0]
new_array = numpy.zeros((100, 300, 3), dtype = numpy.uint8)
sh = new_array.shape
for i in range(sh[0]):
    for j in range(sh[1]):
        for k in range(sh[2]):
            new_array[i][j][k] =random.randint(0,255)
im = Image.fromarray(new_array)
d = ImageDraw.Draw(im)
l = [chr(i+65) for i in range(26)] + [chr(i+97) for i in range(26)]
for i in range(4):
    d.text((75*i + 10 + random.randint(-10, 10), random.randint(0, 40)), random.choice(l), 
           font = ImageFont.truetype("simsun.ttc", 60), 
           fill = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
#im = im.filter(ImageFilter.BLUR)
im.save(path + "/0010.jpg")