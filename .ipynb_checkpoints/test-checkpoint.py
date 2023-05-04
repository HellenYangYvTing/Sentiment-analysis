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
SVM分类器
'''

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import time
start_time = time.time()

import matplotlib.pyplot as plt
min = 1
max = 3
test1 = []
test2 = []



for i in range(min, max):
    #创建模型
    SVM = SVC(C=1.0,kernel='rbf',gamma='auto')
    #拟合数据
    SVM.fit(train_x_tfvec,train_y)
    #训练集
    pre_train_y = SVM.predict(train_x_tfvec)
    train_accuracy = accuracy_score(pre_train_y,train_y)
    #测试集
    pre_test_y = SVM.predict(test_x_tfvec)
    test_accuracy = accuracy_score(pre_test_y,test_y)
    test1.append(train_accuracy)
    test2.append(test_accuracy)

plt.plot(range(min+1,max+1), test1, color = 'red', label = " max_depth_train")
plt.plot(range(min+1,max+1), test2, color = 'blue', label = " max_depth_test")
plt.legend()
plt.show()
print('使用Tf-idf提取特征后使用SVM分类器的准确率\n训练集：{0}\n测试集：{1}'.format(train_accuracy,test_accuracy))
end_time = time.time()
print('使用SVM分类器程序运行时间：',end_time-start_time)