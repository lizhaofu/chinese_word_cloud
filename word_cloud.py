#!/usr/bin/env python 3.6
# -*- coding: utf-8 -*-
"""
# @Company ：华中科技大学机械学院数控中心
# @version : V1.0
# @Author  : lizhaofu
# @contact : lizhaofu0215@163.com  2018--2022
# @Time    : 2020/2/26 21:13
# @File    : word_cloud.py
# @Software: PyCharm
"""

#引入所需要的包
import jieba
import pandas as pd
import numpy as np
from scipy.misc import imread

import matplotlib.pyplot as plt
#定义文件路径
from wordcloud import WordCloud, ImageColorGenerator

from wc_show import wc_show

dir =  "wordcloud/"
#定义语料文件路径
file = "".join([dir, "data_preprocessing1.csv"])
#定义停用词文件路径
stop_words = "".join([dir, "stopwords.txt"])
#定义wordcloud中字体文件的路径
simhei = "".join([dir, "simhei.ttf"])
#读取语料
df = pd.read_csv(file, encoding='utf-8')
df.head()
#如果存在nan，删除
df.dropna(inplace=True)
#将content一列转为list
content=df.content.values.tolist()
#用jieba进行分词操作
segment=[]
for line in content:
    try:
        segs = jieba.cut_for_search(line)
        segs = [v for v in segs if not str(v).isdigit()]#去数字
        segs = list(filter(lambda x:x.strip(), segs))   #去左右空格
        #segs = list(filter(lambda x:len(x)>1, segs)) #长度为1的字符
        for seg in segs:
            if len(seg)>1 and seg != '\r\n':
                segment.append(seg)
    except:
        print(line)
        continue
#分词后加入一个新的DataFrame
words_df=pd.DataFrame({'segment': segment})
#加载停用词
stopwords=pd.read_csv(stop_words, index_col=False, quoting=3, sep="\t", names=['stopword'], encoding='utf-8')
#安装关键字groupby分组统计词频，并按照计数降序排序
words_stat=words_df.groupby(by=['segment'])['segment'].agg({"计数": np.size})
# print(words_stat)
words_stat=words_stat.reset_index().sort_values(by=["计数"], ascending=False)
# print(words_stat)
#分组之后去掉停用词
words_stat=words_stat[~words_stat.segment.isin(stopwords.stopword)]
# print(words_stat.segment)
# print("-------")
# print(words_stat[0:50])
#
# print(type(words_stat))
# with open("data/top_50.csv", 'w', encoding='utf-8') as f:
#     f.write("词语" + "," + "频次" + '\n')
#     for n in range(50):
#         f.write(words_stat[n] + '\n')
#下面是重点，绘制wordcloud词云，这一提供2种方式
#第一种是默认的样式
wordcloud = WordCloud(font_path=simhei, background_color="white", max_font_size=80)
word_frequence = {x[0]:x[1] for x in words_stat.head(200).values}
print(word_frequence)
print(type)
with open("data/top_50.csv", 'w', encoding='utf-8') as f:
    f.write("词语" + "," + "频次" + '\n')
    for k, v in dict(word_frequence).items():
        f.write(k + "," + str(v) + '\n')
# wc_show(dict(word_frequence))
my_wordcloud = WordCloud(
                     background_color='white',  # 设置背景颜色
                     max_words=3000,  # 设置最大现实的字数
                     font_path=simhei,  # 设置字体格式
                     width=1024,
                     height=700,
                     scale=6.0,
                     max_font_size=300,  # 字体最大值
                     random_state=42)
wordcloud = my_wordcloud.fit_words(word_frequence)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
wordcloud.to_file(r'wordcloud_xiangshan_7.jpg')  #保存结果


#第二种是自定义图片
text = " ".join(words_stat['segment'].head(100).astype(str))
abel_mask = imread(r"hongye.png")  #这里设置了一张中国地图
wordcloud2 = WordCloud(background_color='white',  # 设置背景颜色
                     mask = abel_mask,  # 设置背景图片
                     max_words = 3000,  # 设置最大现实的字数
                     font_path = simhei,  # 设置字体格式
                     width=2048,
                     height=1024,
                     scale=5.0,
                     max_font_size=100,  # 字体最大值
                     random_state=42).generate(text)

# 根据图片生成词云颜色
# image_colors = ImageColorGenerator(abel_mask)
# wordcloud2.recolor(color_func=image_colors)
# 以下代码显示图片
plt.imshow(wordcloud2)
plt.axis("off")
plt.show()
wordcloud2.to_file(r'wordcloud_xiangshan_4.jpg') #保存结果

