import numpy as np # numpy数据处理库
import wordcloud # 词云展示库
from PIL import Image # 图像处理库
import matplotlib.pyplot as plt # 图像展示库
from random import randint

def wc_show(word_counts):
    """词云展示"""

    def random_color_func(word=None, font_size=None, position=None, orientation=None, font_path=None,
                          random_state=None):
        """自定义字体色调的函数"""
        rand_sum = randint(1, 5)   #使主色调为红黄
        if rand_sum == 1:
            h = 45   #选取色调范围
        else :
            h = randint(10, 15)
        s = int(100.0 * 255.0 / 255.0)
        l = int(100.0 * float(randint(60, 120)) / 255.0)
        return "hsl({}, {}%, {}%)".format(h, s, l)

    mask = np.array(Image.open('111.jpg'))  # 定义词频背景
    wc = wordcloud.WordCloud(
        font_path='wordcloud/simhei.ttf',  # 设置字体格式
        mask=mask,  # 设置背景图
        max_words=200,  # 最多显示词数
        max_font_size=100,  # 字体最大值
        background_color="white"
    )
    wc.scale = 4   #改善分辨率
    wc.color_func = random_color_func  #自定义字体色调
    wc.generate_from_frequencies(word_counts)  # 从字典生成词云
    wc.to_file('词云3.jpg')  # 保存为背景图1
    image_colors = wordcloud.ImageColorGenerator(mask)  # 从背景图建立颜色方案
    wc.recolor(color_func=image_colors)  # 将词云颜色设置为背景图方案
    plt.imshow(wc)  # 显示词云
    plt.axis('off')  # 关闭坐轴
    plt.show() # 显示图像