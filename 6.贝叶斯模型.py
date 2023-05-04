#1.首先将包导入
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import model_selection

#2.读取数据
data = pd.read_csv('评论汇总-分词后.csv',index_col=0)

#3.划分数据集
train_x, test_x, train_y, test_y = model_selection.train_test_split(data.分词.values.astype('U'),data.分数.values,test_size=0.1,random_state=1)
#划分完毕，查看数据形状
print(train_x.shape,test_x.shape)

#4.使用TfidfVectorizer()对数据进行特征提取，放到模型进行训练
#银镜TF-IDF的包
TF_Vec = TfidfVectorizer(max_df=0.8,
                         min_df=3
                         )
#拟合数据，将数据标准化，一般使用在训练集中
train_x_tfvec = TF_Vec.fit_transform(train_x)
#通过中心化和缩放实现标准化，一般使用在测试集中
test_x_tfvec = TF_Vec.transform(test_x)

'''
5.开始训练模型
Decison Tree Classifier 决策树
'''
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import time
start_time = time.time()
#创建模型
Bys = MultinomialNB()
#拟合数据
Bys.fit(train_x_tfvec,train_y)
#在训练时查看训练集的准确率
pre_train_y = Bys.predict(train_x_tfvec)
#在训练集上的准确率
train_accuracy = accuracy_score(pre_train_y,train_y)
#训练结束 查看预测 输入测试集查看预测
pre_test_y = Bys.predict(test_x_tfvec)
#查看在测试集上的准确率
test_accuracy = accuracy_score(pre_test_y, test_y)
print('使用tf-idf提取特征值后使用贝叶斯分类器的准确率\n训练集：{0}\n测试集：{1}'.format(train_accuracy,test_accuracy))
end_time = time.time()
print('使用贝叶斯分类器的程序运行时间为：',end_time-start_time)