#!/usr/bin/env python
#coding: utf-8

myPath = "C:\\Users\\Lenovo\\Desktop\\"
fontPath = "C:\\Windows\\Fonts\\" #win10上系统的字体位置
inputFile = "1_sirwill.jpg"
outputFile = "output.jpg"

from Pillow import Image, ImageDraw,ImageFont
#打开图片
im = Image.open(myPath + inputFile)  #打开一个照片对象
draw = ImageDraw.Draw(im)            #创建画布

#根据图片大小确定字体大小
fontsize = (min(im.size)/4          #注意truetype方法要整数，需要取整

#加文字
#实例
font = ImageFont.truetype(fontPath + 'ALGER.TTF',fontsize) #其余参数默认 得到字体实例
draw.text((im.size[0]-fontsize,0), '5', font = font, fill = (256, 0, 0)) #确定位置、数字、实例、填充色
#保存图片
im.save(myPath + outputFile,"jpeg")