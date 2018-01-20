#！/usr/bin/env python
#coding: utf-8
#实现两层图像叠加后再添加数字
from PIL import Image, ImageDraw,ImageFont

def white_to_transparent(img):
    img = img.convert('RGBA') #返回一个转换后的图像的副本
    datas = img.getdata()
    newData=[]
    for item in datas:
        if item[0] == 255 and item[1] ==255:
                newData.append((255,255,255,0))
        else:
            newData.append(item)
    img.putdata(newData)    #赋给图片新的像素数据
    return img



if __name__ == "__main__":
    myPath  = "C:\\Users\\Lenovo\\Desktop\\"
    fontPath = "C:\\\Windows\\\Fonts\\"
    inputFile1 = "1.jpg"
    inputFile2 = "2.jpg"
    outputFile = "output.jpg"

    #打开两张图片，注意路径
    inputFile1_image = Image.open(myPath + inputFile1)
    inputFile2_image = Image.open(myPath + inputFile2)

    inputFile2_transparent = white_to_transparent(inputFile2_image)
    inputFile1_image.paste(inputFile2_transparent, (0,0), inputFile2_transparent)

    fontsize = int(min(inputFile1_image.size)/4)         #注意为整数
    font = ImageFont.truetype(fontPath+'ALGER.TTF', fontsize)

    draw = ImageDraw.Draw(inputFile1_image) #在p1_image上绘制文字图像
    draw.text((inputFile1_image.size[0]-fontsize,0), u'8', font = font)
    inputFile1_image.save(myPath + outputFile,"PNG")     #由于使用RGBA模块，则要转换成PNG格式



