#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 将0002题目中随机生成的验证码保存到Redis 数据库
import uuid
import redis

r = redis.Redis(host='localhost', port=6379, db=0)  #需要提前安装redis数据库
# 生成 num 个验证码，每个长度为length，可设置默认长度
def create_num(num, length=16):
    result = []
    while num > 0:
        uuid_id = uuid.uuid4()
        # 删去字符串中的'-',取出前length 个字符
        temp = str(uuid_id).replace('-', '')[:length]
        if temp not in result:
            result.append(temp)
            num -= 1
    return result


# 保存到Redis数据库
def save_to_redis(num_list):
    for code in num_list:
        r.lpush('code', code)

save_to_redis(create_num(200))

for item in r.lrange('code',0,-1):  #输出保存在redis数据库中code列表的内容
    print(item)
