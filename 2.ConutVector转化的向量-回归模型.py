#1.首先将要用到的包进行导入
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import model_selection


#2.读取数据
data = pd.read_csv('评论汇总-分词后.csv', index_col=0)

#3.划分数据集
'''
备注：将“评论”数据当做X，将“评分”数据当做Y。将数据集划分成训练数据与测试数据，训练数据用来训练机器学习算法，测试数据用于检测通过训练数据训练出来的算法的效果。
    划分数据集的时候需要用到sklearn中的model_selection中的train_test_split()方法。
    需要传入的参数为“评论文本”、“文本的评分”（这里的好评还是差评对应的数字）、test_size表示是划分数据集与训练集的比例，根据划分的比例，将数据划分为10等分，测试集占据其中一份。
    shuffle的作用是在划分数据集时，会将数据顺序打乱。
train_x:训练数据集
test_x:测试数据集
train_y:训练数据集的标签
test_y:测试数据集的标签
random_state:这是为了在不同的环境中，保证随机数取值一致，以便验证模型的效果
'''
train_x,test_x,train_y,test_y = model_selection.train_test_split(data.分词.values.astype('U'),data.分数.values,test_size=0.1,random_state=1)
#划分完毕，查看数据形状
print(train_x.shape,test_y.shape)

def get_stopwords(stop_word_file):
    custom_stopwords_list = [line.strip() for line in open(stop_word_file, encoding='UTF-8').readlines()]
    return custom_stopwords_list

#获得由停用词组成的列表
stop_words_file = 'cn_stopwords.txt'
stopwords = get_stopwords(stop_words_file)
#4. CountVectorizer()分别进行特征提取
#开始使用 CountVectorizer()分别进行特征提取。他可以依据词语出现评率转化向量。并且加入去除停用词，这里数据集已经去除停用词，所以没有使用
CT_Vec =  CountVectorizer(max_df=0.8, #在超过这一比例的文档中出现的关键词（过于平凡），去除掉
                          min_df=3,   #在低于这一数量的文档中出现关键词（过于独特），去除掉
                          token_pattern=u'(?u)\\b[^\\d\\W]\\w+\\b',#使用正则表达式，去除想去的内容
                          stop_words=frozenset(stopwords))
#拟合数据，将数据转化为标准形式，一般在使用在训练集中
train_x_ctvec = CT_Vec.fit_transform(train_x)
#通过中心化和缩放现实标准化，一般使用在测试集中
test_x_ctvec = CT_Vec.transform(test_x)

#5.使用ConutVector转化的向量作为特征传入逻辑回归模型
#构造模型之前首先将包进行导入
from sklearn import linear_model
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split,GridSearchCV
import time
start_time = time.time()
#创建模型
print("无优化")
model = linear_model.LogisticRegression(penalty='l2',C=1,solver='liblinear',max_iter=1000,multi_class='ovr')
#进行模型的优化，因为一些参数是不确定的，所以就让模型自己在训练中去确定自己的参数 模型的名字也由LR转为model
'''
model = GridSearchCV(lr, cv=3,param_grid={
    'C':np.logspace(0,4,30),
    'penalty':['l1','l2']
})
'''

#模型拟合CountVectorizer拿到数据
model.fit(train_x_ctvec,train_y)
#查看自己拟合的最优化参数
#print("最优化参数:",model.best_params_)
#在训练时查看数据集的准确率
pre_train_y = model.predict(train_x_ctvec)
#在训练集上的正确率
train_accuracy = accuracy_score(pre_train_y,train_y)
#训练结束查看预测 输入测试集查看预测
pre_test_y = model.predict(test_x_ctvec)
#查看在测试集上的准确率
test_accuracy = accuracy_score(pre_test_y,test_y)
print("使用CountVectorizer提取特征使用逻辑回归，让模型自适应参数，进行模型优化\n训练集：{0}\n测试集：{1}".format(train_accuracy,test_accuracy))
end_time = time.time()
print("使用模型优化的程序运行时间为：",end_time-start_time)