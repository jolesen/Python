#!/usr/bin/env python
#coding: utf-8
#生成激活码
import random

def gen_code(length=8):
    code_list = []
    for i in list(range(10)):
        code_list.append(str(i))
            #print i
        print(code_list)
    for i in list(range(65, 91)):
        code_list.append(chr(i))
        print(code_list)
            #print chr(i)
    for i in list(range(97, 123)):
        code_list.append(chr(i))
        print(code_list)

    myslice = random.sample(code_list, length) #可以从指定的序列中，随机的截取指定长度的片断，不作原地修改
    veri_code = ''.join(myslice) #将字符序列进行连接

    return veri_code

if __name__ == "__main__":
  #  for i in range(10):
        print(gen_code(8))



