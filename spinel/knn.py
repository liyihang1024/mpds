from sklearn.neighbors import KNeighborsClassifier    # 导入sklearn.neighbors模块中KNN类
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split

data = pd.read_excel("spinel.xlsx",sheet_name=1,index_col=None,header = [1],usecols=None)
X = data.iloc[:,:-2]
y = data.iloc[:,-2:-1]
X_train,X_test, y_train, y_test =train_test_split(X,y,test_size=0.3,random_state=0)

print(X_train)
print(X_test)
print(y_train)
print(y_test)

knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
y_predict = knn.predict(X_test)
score = knn.score(X_test, y_test, sample_weight=None)

print('y_predict = ')
print(y_predict)                                 # 输出测试的结果
print('y_test = ')
print(np.array(y_test))                                    # 输出原始测试数据集的正确标签，以方便对比
print('Accuracy:%.2f'%score)

print('正尖晶石数 ：', data.Label.value_counts()[1])
print('反尖晶石数 ：', data.Label.value_counts()[0])

name_list = ['Normal spinel', 'Inverse spinel']
num_list = [52.4, 57.8, 59.1, 54.6]
plt.figure(figsize=(7,5))
sns.set(style="darkgrid")
sns.countplot(x='Label', hue ='Spinel', data=data)
plt.title('Spinel Label Histogram')
plt.xlabel('Label')
plt.ylabel('Frequency')
plt.show()
