'''
数据清洗：
1.去除重复评论
2.对评论进行分词
'''
import numpy as np
import pandas as pd

#去除重复值:True表示直接在源数据上进行操作
data = pd.read_csv('JDcontents_vivo.csv')

data.drop_duplicates(inplace = True)
