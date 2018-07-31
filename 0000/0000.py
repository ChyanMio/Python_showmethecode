# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
from PIL import Image, ImageDraw, ImageFont
path = os.path.split(os.path.realpath(__file__))[0]
font = ImageFont.truetype('simsun.ttc', 24)
image = Image.open(path + "/weibo.jpg")
draw = ImageDraw.Draw(image)
draw.text((150, 6), '4', fill = (255, 0, 0), font = font)
image.save(path + "/0000.jpg")