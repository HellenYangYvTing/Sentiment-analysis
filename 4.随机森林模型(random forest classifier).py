#首先将用到的包进行导入
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn import model_selection

#将数据进行读取
data=pd.read_csv('评论汇总-分词后.csv',index_col=0)

# 现在是划分数据集
train_x, test_x, train_y, test_y = model_selection.train_test_split(data.分词.values.astype('U'), data.分数.values,
                                                                    test_size=0.1, random_state=1)
# 划分完毕，查看数据形状
print(train_x.shape, test_x.shape)
# train_x 训练集数据 test_x 测试集数据  train_y训练集的标签 test_y 测试集的标签
#定义函数，从哈工大中文停用词表里面，把停用词作为列表格式保存并返回 在这里加上停用词表是因为TfidfVectorizer和CountVectorizer的函数中
'''
使用TfidfVectorizer()对数据进行特征的提取，投放到不同的模型中进行实验
'''
# 开始使用TF-IDF进行特征的提取，对分词后的中文语句做向量化。
# 引进TF-IDF的包
TF_Vec = TfidfVectorizer(max_df=0.8,
                         min_df=3
                         )
# 拟合数据，将数据准转为标准形式，一般使用在训练集中
train_x_tfvec = TF_Vec.fit_transform(train_x)
# 通过中心化和缩放实现标准化，一般使用在测试集中
test_x_tfvec = TF_Vec.transform(test_x)

'''
开始训练random forest classifier (随机森林)模型
'''
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import time
start_time = time.time()
#创建模型
Rfc = RandomForestClassifier(n_estimators=8)
#拟合从TfidfVectorizer()中拿到的数据
Rfc.fit(train_x_tfvec,train_y)
#在训练时查看训练集的准确率
pre_train_y = Rfc.predict(train_x_tfvec)
#在训练集上的准确率
train_accuracy = accuracy_score(pre_train_y,train_y)
#在训练时查看测试集的准确率
pre_test_y = Rfc.predict(test_x_tfvec)
#在测试集上的正确率
test_accuracy = accuracy_score(pre_test_y,test_y)
print('使用TfidfVectorizer提取特征使用随机森林分类器的准确率\n训练集：{0}\n测试集：{1}'.format(train_accuracy,test_accuracy))
end_time = time.time()
print('使用随机森林分类器的程序运行时间为：',end_time - start_time)