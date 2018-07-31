# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 16:53:02 2018

@author: zhang
"""

import random
list=[]
#生成26个大写的字母
for x in range(65,91):
    a=str(chr(x))  #生成对应的ASCII码对应的字符串
    list.append(a)
#生成26个小写字母
for x in range(97,123):
    a=str(chr(x))  #生成对应的ASCII码
    list.append(a)     
#生成10个数字
for x in range(10):
    list.append(str(x))
'''
def gen_code():
    a=random.sample(list,16)
    print a
'''
#生成16位激活码
def gen_code():
    s=''
    for x in range(16):
        a=random.choice(list)
        s=s+a
    print(s)

#生成200个激活码
for x in range(200):
    gen_code()