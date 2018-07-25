# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from PIL import Image, ImageDraw, ImageFont
font = ImageFont.truetype('simsun.ttc', 24)
image = Image.open(r"C:\USers\zhang\Documents\ShowMeTheCode\0000\weibo.jpg")
draw = ImageDraw.Draw(image)
draw.text((150, 6), '4', fill = (255, 0, 0), font = font)
image.show()