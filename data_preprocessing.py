#!/usr/bin/env python 3.6
# -*- coding: utf-8 -*-
"""
# @Company ：华中科技大学机械学院数控中心
# @version : V1.0
# @Author  : lizhaofu
# @contact : lizhaofu0215@163.com  2018--2022
# @Time    : 2020/2/26 21:29
# @File    : data_preprocessing.py
# @Software: PyCharm
"""
import os
# conferences = []
# with open("data/XIANGSHAN_SCIENCE_CONFERENCE-1.txt", 'r', encoding='utf-8') as f:
#     conference = []
#     for line in f.readlines():
#         cont = line.strip().split("|")
#         conferences.append(cont)
#
#
# with open("wordcloud/data_preprocessing1.csv", 'w', encoding='utf-8') as f:
#     f.write("num" + "," + "theme" + "," + "date" + "," + "content" + '\n')
#     for n in conferences:
#         f.write(n[0] + "," + str(n[1]) + "," + n[2] + "," + n[3] + '\n')
#
# # num =[]
# # for n in conferences:
# #     if "S" in n[0]:
# #         num.append(n[0])
# #
# # print(len(num))
#
# # print(conferences[328])
#
# years = []
# for con in conferences:
#     year = con[2].split('-')[0]
#     years.append(year)
#
#
# c = sorted(list(set(years)), reverse=True)
# print(c)
# step = 3
#
# d = [c[i:i+step] for i in range(0, len(c), step)]
#
# print(d)
# for i in d:
#     file_name = str(i)
#     with open("three_years/" + file_name+".csv", 'w', encoding='utf-8') as f:
#         f.write("num" + "," + "theme" + "," + "date" + "," + "content" + '\n')
#         for y in i:
#             for n in conferences:
#                 if y in n[2]:
#                     f.write(n[0] + "," + str(n[1]) + "," + n[2] + "," + n[3] + '\n')
import re

from word_cloud_show import open_folder


def data_preprocess(file_path, output):
    conferences = []
    with open(file_path, 'r', encoding='utf-8') as f:
        conference = []
        for line in f.readlines():
            cont = line.strip().split("|")
            conferences.append(cont)

    if not os.path.exists(output):
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(output)
    filename = file_path.split("/")[1].split('.')[0]
    with open(output + '/' + filename + ".csv", 'w', encoding='utf-8') as f:
        f.write("num" + "," + "theme" + "," + "date" + "," + "content" + '\n')
        for n in conferences:
            if ',' in n[1]:
                s = re.sub(r',', '，', n[1])
                f.write(n[0] + "," + str(s) + "," + n[2] + "," + n[3] + '\n')
            else:
                f.write(n[0] + "," + str(n[1]) + "," + n[2] + "," + n[3] + '\n')


file_list = open_folder("DATA-主题划分结果-wzh-20200226")
print(file_list)
for n in file_list:
    data_preprocess(n, "预处理-DATA-主题划分结果-wzh-20200226")















