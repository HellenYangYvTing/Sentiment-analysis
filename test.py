import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('3result.csv')

#统计数据长度，包括最小长度、最大长度、平均长度。
df["length"] = df['评论'].apply(len)
df2 = df.length.value_counts()     # 可以通过df.colname 来指定某个列，value_counts()在这里进行计数
#print(df)
print(df2)
print(df.length.max())
print(df.length.min())
#x = np.arange(df.length.min(),df.length.max(),1)
