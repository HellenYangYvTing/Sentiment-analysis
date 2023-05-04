import numpy as np
import pandas as pd

df = pd.read_csv('评论汇总-utf.csv')
#2去除重复评论
df.drop_duplicates(inplace=True) #直接在数据集上进行删除
print(df.shape)

#3.去除默认评论，以及长度过短无效评论
df = df[~df['评论'].isin(['您没有填写内容，默认好评'])]
df = df[~df['评论'].isin(['此用户未填写评价内容'])]
for i in df['评论'].loc[:]:
    print(i)
    if len(str(i)) <= 5 or len(str(i)) >512:
        print(i)
        df = df[~df['评论'].isin([i])]


#4对数据进行分类（1为差评，2-4为中评，5为好评）
df.loc[df['评分']==3,'评分'] = 2
df.loc[df['评分']==4,'评分'] = 2
df.loc[df['评分']==5,'评分'] = 3

#排序 按照列排序数据，默认升序排列
df = df.sort_values('评分')

#不保存和列索引，使用NULL来替代空字符串(行索引：header=False)
df.to_csv("评论汇总-预处理.csv",index=False,na_rep="NULL")
