#!/usr/bin/env python 3.6
# -*- coding: utf-8 -*-
"""
# @Company ：华中科技大学机械学院数控中心
# @version : V1.0
# @Author  : lizhaofu
# @contact : lizhaofu0215@163.com  2018--2022
# @Time    : 2020/2/27 09:38
# @File    : word_cloud_show.py
# @Software: PyCharm
"""


import os
#引入所需要的包
import jieba
import pandas as pd
import numpy as np
from scipy.misc import imread
from wordcloud import WordCloud, ImageColorGenerator

import matplotlib.pyplot as plt


# 读取文件夹下的文件，返回相对路径，并存储为list，输入参数为一个文件夹的相对路径或绝对路径
def open_folder(folder_dir):
    file_list = []
    for file in os.listdir(folder_dir):
        temp = os.path.join(folder_dir, file)
        # print(temp)
        file_list.append(temp)
    return file_list


def word_cloud_show(file_path, output):

    # 定义停用词文件路径
    stop_words = "wordcloud/stopwords.txt"
    # 定义wordcloud中字体文件的路径
    simhei_path = "wordcloud/simhei.ttf"
    # 读取语料
    df = pd.read_csv(file_path, encoding='utf-8')
    df.head()
    # 如果存在nan，删除
    df.dropna(inplace=True)
    # 将content一列转为list
    content = df.content.values.tolist()
    # 用jieba进行分词操作
    segment = []
    for line in content:
        try:
            segs = jieba.cut_for_search(line)
            segs = [v for v in segs if not str(v).isdigit()]  # 去数字
            segs = list(filter(lambda x: x.strip(), segs))  # 去左右空格
            # segs = list(filter(lambda x:len(x)>1, segs)) #长度为1的字符
            for seg in segs:
                if len(seg) > 1 and seg != '\r\n':
                    segment.append(seg)
        except:
            print(line)
            continue

    # 分词后加入一个新的DataFrame
    words_df = pd.DataFrame({'segment': segment})
    # 加载停用词
    stopwords = pd.read_csv(stop_words, index_col=False, quoting=3, sep="\t", names=['stopword'], encoding='utf-8')
    # 安装关键字groupby分组统计词频，并按照计数降序排序
    words_stat = words_df.groupby(by=['segment'])['segment'].agg({"计数": np.size})
    # print(words_stat)
    words_stat = words_stat.reset_index().sort_values(by=["计数"], ascending=False)
    # print(words_stat)
    # 分组之后去掉停用词
    words_stat = words_stat[~words_stat.segment.isin(stopwords.stopword)]

    # 下面是重点，绘制wordcloud词云，这一提供2种方式
    # 第一种是默认的样式
    wordcloud = WordCloud(font_path=simhei_path, background_color="white", max_font_size=80)
    word_frequence = {x[0]: x[1] for x in words_stat.head(200).values}
    word_frequence_top_50 = {x[0]: x[1] for x in words_stat.head(50).values}
    # print(word_frequence)
    # print(type)
    if not os.path.exists(output):
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(output)
    filename = file_path.split("/")[1].split('.')[0]
    with open(output + '/' + filename + "top_50.csv", 'w', encoding='utf-8') as f:
        f.write("词语" + "," + "频次" + '\n')
        for k, v in dict(word_frequence_top_50).items():
            f.write(k + "," + str(v) + '\n')
    # wc_show(dict(word_frequence))
    my_wordcloud = WordCloud(
        background_color='white',  # 设置背景颜色
        max_words=3000,  # 设置最大现实的字数
        font_path=simhei_path,  # 设置字体格式
        width=1024,
        height=700,
        scale=6.0,
        max_font_size=300,  # 字体最大值
        random_state=42)
    wordcloud = my_wordcloud.fit_words(word_frequence)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
    wordcloud.to_file(output + '/' + filename + '词云图.jpg')  # 保存结果


if __name__ == "__main__":
    file_list = open_folder("three_years")
    # print(file_list)
    for n in file_list:
        word_cloud_show(n, "iteration_2_three_years_result")

    file_list = open_folder("all")
    # print(file_list)
    for n in file_list:
        word_cloud_show(n, "iteration_2_all_result")

    file_list = open_folder("预处理-DATA-主题划分结果-wzh-20200226")
    # print(file_list)
    for n in file_list:
        word_cloud_show(n, "iteration_2_topic_result")

