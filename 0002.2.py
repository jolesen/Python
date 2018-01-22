#!/usr/bin/env python
# -*- coding;utf-8 -*-

import uudi
import pymysql

#生成num哥验证码，每个长度为length，可设置默认长度为8
def create_num(num,length = 8):
    result = []
    while num>0:
        uuid_id = uuid.uuid4()
        #删去字符串中的'-'，取出前length个字符
        temp = str(uuid_id).replace('-','')[:length]
        if temp not in result:
            result.append(temp)
            num -= 1
    return result

#保存到MySQL数据库
def save_to_mysql(code):
    conn = pymysql.connect(
        host='localhost',
        port = 3306,
        user = 'root',
        passwd = None,
        db = 'test')
    try:
        with conn.cusor() as cusor:
            #c创建新的纪录
        sql = "INSERT INTO 'codes'('code') VALUES (%s)"
        cursor.execute(sql,code)

        conn.comit()

        with conn.cursor() as cursor:
            #读入单个纪录
            sql = "SELECT 'id', 'code', FROM 'codes' WHERE 'code' =%s"
            cursor.execute(sql,code)
            result = cursor.fetchone()
            print(result)
    finally:
        conn.close()

for code in create_num(200):
    save_to_mysql(coe)




