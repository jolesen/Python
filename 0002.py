#!/usr/bin/env python
#coding: utf-8
#生成激活码
import random

def gen_code(length=8):
    code_list = []
    for i in list(range(10)):
        code_list.append(str(i))
            #print i
    for i in list(range(65, 91)):
        code_list.append(chr(i))
            #print chr(i)
    for i in list(range(97, 123)):
        code_list.append(chr(i))


    myslice = random.sample(code_list, length) #可以从指定的序列中，随机的截取指定长度的片断，不作原地修改
    veri_code = ''.join(myslice) #将字符序列进行连接

    return veri_code

if __name__ == "__main__":

    myPath = "C:\\Users\\Lenovo\\Desktop\\"    #桌面路径
    outputFile = "output.txt"
    f = open(myPath + outputFile, "w")
    num = int(input("请输入你要产生的激活码数量："))
    for i in range(num):
        f.write(gen_code(8) + "\n")           #将激活码写入output.txt里
    f.close()


