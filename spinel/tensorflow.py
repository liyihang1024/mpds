from sklearn.linear_model import SGDRegressor
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.kernel_ridge import KernelRidge
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import MinMaxScaler
from pandas import DataFrame
from sklearn.cross_validation import cross_val_score
from math import sqrt

# 读入数据
data = pd.read_excel("spinel_update.xlsx",sheet_name=0,index_col=None,header = [1],usecols=None)

# 删除有缺失值的行
# data.dropna(inplace=True)

# 将数据分成X和y
X = data.iloc[:,:-8]
y = data.iloc[:,-1]

# 将数据缩放至[0, 1]间。训练过程: fit_transform()
std = MinMaxScaler()
X = DataFrame(std.fit_transform(X))
# data.to_excel("spinel_Standardization.xlsx",sheet_name='Standardization')

X_train,X_test, y_train, y_test =train_test_split(X,y,test_size=0.3,random_state=0)

regr = SGDRegressor(max_iter=1000, penalty=None, eta0=0.1, loss="squared_loss")
regr.fit(X_train, y_train)

# 交叉验证
scores = cross_val_score(regr, X_train, y_train, cv=10)
print ('交叉验证R方值:', scores)
print ('交叉验证R方均值:', np.mean(scores))

# Make predictions using the testing set
y_test_pred = regr.predict(X_test)
y_train_pred = regr.predict(X_train)

print("Mean squared error: %.2f"% sqrt(mean_squared_error(y_test, y_test_pred)))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(y_test, y_test_pred))