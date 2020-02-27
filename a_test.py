#!/usr/bin/env python 3.6
# -*- coding: utf-8 -*-
"""
# @Company ：华中科技大学机械学院数控中心
# @version : V1.0
# @Author  : lizhaofu
# @contact : lizhaofu0215@163.com  2018--2022
# @Time    : 2020/2/26 23:26
# @File    : a_test.py
# @Software: PyCharm
"""

# a = [1,2,3,4,5,6,7,8,9,10,11]
# # c = sorted(a, reverse=True)
# # print(c)
# # step = 3
# # b = [a[i:i+step] for i in range(0,len(a),step)]
# # d = [c[i:i+step] for i in range(0,len(a),step)]
# # print(b)
# # print(d)
import re
s ="string, With. Punctuation?"
s = re.sub(r',','，',s)
print(s)