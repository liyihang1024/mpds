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

# 读入数据
data = pd.read_excel("spinel.xlsx",sheet_name=3,index_col=None,header = [1],usecols=None)

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
# print(X_train)
# print(X_test)
# print(y_train)
# print(y_test)

# Create linear regression object
regr = linear_model.LinearRegression()
# regr = linear_model.Ridge(alpha = .05)
# regr = linear_model.RidgeCV(alphas=[0.01, 0.02, 0.03, 0.04, 0.05, 0.1, 1.0, 5.0, 10.0])  # RidgeCV 通过内置的 Alpha 参数的交叉验证来实现岭回归
# regr = linear_model.BayesianRidge()
# regr = KernelRidge(alpha=.001,kernel='rbf')
# regr = RandomForestRegressor()
# regr = SVR(kernel='rbf',C=100, gamma=.2)

# Train the model using the training sets
regr.fit(X_train, y_train)

# Make predictions using the testing set
y_test_pred = regr.predict(X_test)
y_train_pred = regr.predict(X_train)

# The coefficients and intercept
# print('Coefficients: \n', regr.coef_)
# print('Intercept:',regr.intercept_)
# The mean squared error
print("Mean squared error: %.2f"% mean_squared_error(y_test, y_test_pred))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(y_test, y_test_pred))

# print('alpha:',regr.alpha_)

# Plot outputs
plt.figure(figsize=(7, 5))
plt.scatter(y_train,y_train_pred, color='black',label='TrainSet')
plt.scatter(y_test, y_test_pred, color='red',label='TestSet')
plt.plot([-600,-250],[-600,-250])
plt.xlabel('y_test')
plt.ylabel('y_pred')
plt.xticks()
plt.yticks()
plt.title('Final Energy/Atom(eV)')
plt.legend(loc='upper left')           # plt.legend()添加图例
# plt.savefig("BayesianRidge")
plt.show()