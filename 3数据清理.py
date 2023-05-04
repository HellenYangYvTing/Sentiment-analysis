import pandas as pd
import re
df = pd.read_csv('评论汇总-utf.csv')
#1数据去重，删除自己负责数据中的重复数据
df.drop_duplicates(inplace=True)

#2.数据缺失值处理
df.dropna(inplace=True)
'''
#3.去除无用字符，包括英文字母和数字、表情符号和其他字符、冒号和空白
for i in range(df.shape[0]):
    df.iloc[i,0] = re.sub('[a-zA-Z0-9、，,！!@；+~ ！@￥……&*（）————+=、|】}【{：；“‘《》·。？%：——（）*.?: ]','',df.iloc[i,0] )

for i in df['评论'].loc[:]:
    if len(i) <= 5 or len(i) >512:
        df = df[~df['评论'].isin([i])]



#4.统计数据长度，包括最小长度、最大长度、平均长度。
df["length"] = df['评论'].apply(len)
df2 = df.length.value_counts()  # 可以通过df.colname 来指定某个列，value_counts()在这里进行计数
print("数据长度     长度出现次数")
print(df2)
print('最大长度：',df.length.max())
print('最小长度',df.length.min())
#删除生成的length列
df.drop('length',axis = 1, inplace=True)#改变原始数据

#5.统计好评、中评、差评的评论数量，查看数据是否均衡，
df3 = df.分数.value_counts()  # 可以通过df.colname 来指定某个列，value_counts()在这里进行计数
print("数据均衡性查看,删除前：")
print(df3)

#删除不均衡的部分,删除行
df.reset_index(drop=True, inplace=True)
df = df.drop(labels=range(10000,11512), axis=0)
df = df.drop(labels=range(6000,6287), axis=0)
df = df.drop(labels=range(2,74), axis=0)
df3 = df.分数.value_counts()  # 可以通过df.colname 来指定某个列，value_counts()在这里进行计数
print("数据均衡性查看,删除后：")
print(df3)
print('数据形态',df.shape)
'''

df = df.sort_values('分数')
print(df.shape)
#df = df.drop(labels=range(df.shape[0] -2,df.shape[0]+1), axis=0)
df = df.drop(df.index[df.shape[0]-1])
#不保存和列索引，使用NULL来替代空字符串(行索引：header=False)
df.to_csv("评论汇总-清洗后.csv",index=False,na_rep="NULL")
