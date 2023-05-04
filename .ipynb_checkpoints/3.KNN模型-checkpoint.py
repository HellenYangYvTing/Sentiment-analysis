#首先将用到的包进行导入
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn import model_selection

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

'''
使用KNN模型
'''
import time
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
start_time = time.time()
#创建模型
Kn = KNeighborsClassifier()
#拟合从tf-idf拿到的数据
Kn.fit(train_x_tfvec,train_y)
#在训练时查看训练集的准确率
pre_train_y = Kn.predict(train_x_tfvec)
#在训练集上的正确率
train_accuracy = accuracy_score(pre_train_y,train_y)
#训练结束查看预测 输入测试集查看预测
pre_test_y = Kn.predict(test_x_tfvec)
#查看在测试集上的准确率
test_accuracy = accuracy_score(pre_test_y,test_y)
print('使用TfidfVectorizer提取特征使用KNN分类器的准确率\n训练集：{0}\n测试集：{1}'.format(train_accuracy,test_accuracy))
end_time = time.time()
print('使用KNN分类器的程序运行时间为：',end_time - start_time)
