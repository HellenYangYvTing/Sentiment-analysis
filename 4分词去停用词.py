import jieba
import pandas as pd

# 创建停用词列表
def stopwordslist():
    stopwords = [line.strip() for line in open('cn_stopwords.txt',encoding='UTF-8').readlines()]
    return stopwords
# 对句子进行中文分词
def seg_depart(sentence):
    # 对文档中的每一行进行中文分词
    print("正在分词")
    sentence_depart = jieba.cut(sentence.strip())
    # 创建一个停用词列表
    stopwords = stopwordslist()
    # 输出结果为outstr
    outstr = ''
    # 去停用词
    #print('分词后', sentence_depart)
    for word in sentence_depart:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr

df = pd.read_csv('评论汇总-分词后.csv')
'''
df["分词"] = df['评论'].apply(len)
for i in range(df.shape[0]):
     print(df.iloc[i,0])
     inputs = df.iloc[i,0]
     line_seg = seg_depart(inputs)
     df.iloc[i, 2] = line_seg
     print(i,'去除无用后',line_seg)
'''
df = df.drop(df.index[df.shape[0]-1])
df.to_csv("评论汇总-分词后.csv",index=False,na_rep="NULL")