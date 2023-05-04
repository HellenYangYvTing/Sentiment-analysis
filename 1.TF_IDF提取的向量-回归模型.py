#首先将用到的包进行导入
import pandas as pd
import numpy as np
import jieba
import re
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn import model_selection
from sklearn import preprocessing

#将数据进行读取
data=pd.read_csv('评论汇总-分词后.csv',index_col=0)

# 现在是划分数据集
# random_state 取值，这是为了在不同环境中，保证随机数取值一致，以便验证模型的实际效果。
train_x, test_x, train_y, test_y = model_selection.train_test_split(data.分词.values.astype('U'), data.分数.values,
                                                                    test_size=0.1, random_state=1)

# 划分完毕，查看数据形状
print(train_x.shape, test_x.shape)
# train_x 训练集数据 test_x 测试集数据  train_y训练集的标签 test_y 测试集的标签
#定义函数，从哈工大中文停用词表里面，把停用词作为列表格式保存并返回 在这里加上停用词表是因为TfidfVectorizer和CountVectorizer的函数中
#可以根据提供用词里列表进行去停用词
def get_stopwords(stop_word_file):
    custom_stopwords_list = [line.strip() for line in open(stop_word_file, encoding='UTF-8').readlines()]
    return custom_stopwords_list

#获得由停用词组成的列表
stop_words_file = 'cn_stopwords.txt'
stopwords = get_stopwords(stop_words_file)

'''
使用TfidfVectorizer()和 CountVectorizer()分别对数据进行特征的提取，投放到不同的模型中进行实验
'''
# 开始使用TF-IDF进行特征的提取，对分词后的中文语句做向量化。
# 引进TF-IDF的包
TF_Vec = TfidfVectorizer(max_df=0.8,
                         min_df=3,
                         stop_words=frozenset(stopwords)
                         )
# 拟合数据，将数据准转为标准形式，一般使用在训练集中
train_x_tfvec = TF_Vec.fit_transform(train_x)
# 通过中心化和缩放实现标准化，一般使用在测试集中
test_x_tfvec = TF_Vec.transform(test_x)

# 开始使用CountVectorizer()进行特征的提取。它依据词语出现频率转化向量。并且加入了去除停用词
CT_Vec = CountVectorizer(max_df=0.8,  # 在超过这一比例的文档中出现的关键词（过于平凡），去除掉。
                         min_df=3,  # 在低于这一数量的文档中出现的关键词（过于独特），去除掉。
                         token_pattern=u'(?u)\\b[^\\d\\W]\\w+\\b',  # 使用正则表达式，去除想去除的内容
                         stop_words=frozenset(stopwords))  # 加入停用词)
# 拟合数据，将数据转化为标准形式，一般使用在训练集中
train_x_ctvec = CT_Vec.fit_transform(train_x)
# 通过中心化和缩放实现标准化，一般使用在测试集中
test_x_ctvec = CT_Vec.transform(test_x)

'''
使用TF_IDF提取的向量当作数据特征传入模型
'''
#构建模型之前首先将包进行导入
from sklearn import linear_model
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split, GridSearchCV
import time
start_time=time.time()
#创建模型
model = linear_model.LogisticRegression(penalty='l2', C=1, solver='liblinear', max_iter=1000, multi_class='ovr')
#进行模型的优化，因为一些参数是不确定的，所以就让模型自己在训练中去确定自己的参数 模型的名字也由LR转变为model
'''
model = GridSearchCV(lr, cv=3, param_grid={
        'C': np.logspace(0, 4, 30),
        'penalty': ['l1', 'l2']
    })
'''
print(train_x,train_y)
print(train_x_tfvec,train_y)
#模型拟合tf-idf拿到的数据
model.fit(train_x_tfvec,train_y)
#查看模型自己拟合的最优参数
print('最优参数：', 1)
#在训练时查看训练集的准确率
pre_train_y=model.predict(train_x_tfvec)
#在训练集上的正确率
train_accracy=accuracy_score(pre_train_y,train_y)
#训练结束查看预测 输入验证集查看预测
pre_test_y=model.predict(test_x_tfvec)
#查看在测试集上的准确率
test_accracy = accuracy_score(pre_test_y,test_y)
print('使用TF-IDF提取特征使用逻辑回归,让模型自适应参数，进行模型优化\n训练集:{0}\n测试集:{1}'.format(train_accracy,test_accracy))
end_time=time.time()
print("使用模型优化的程序运行时间为",end_time-start_time)