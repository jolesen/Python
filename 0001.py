#!/usr/bin/env python
#coding: utf-8


myPath = "C:\\Users\\Lenovo\\Desktop\\"
fontPath = "C:\\Windows\\Fonts\\"
inputFile = "1_sirwill.jpg"
outputFile = "output.jpg"

from PIL import Image, ImageFont, ImageDraw
#打开图片
im = Image.open(myPath + inputFile)
draw = ImageDraw.Draw(im)
#根据图片大小确定字体大小
fontsize =  int(min(im.size)/4)
#加文字
font = ImageFont.truetype(fontPath + 'ALGER.TTF', fontsize)
draw.text((im.size[0]-fontsize, 0), '5', font = font, fill = (256,0,0))
im.save(myPath + outputFile,"jpeg")