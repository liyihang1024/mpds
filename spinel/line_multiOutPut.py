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
from math import sqrt


########################## 读入数据并分为trainSet和testSet #################################
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


################################### 选择模型 ############################################
regr_LR = linear_model.LinearRegression()
# regr_R = linear_model.Ridge(alpha = .05)
regr_RCV = linear_model.RidgeCV(alphas=[0.01, 0.02, 0.03, 0.04, 0.05, 0.1, 1.0, 5.0, 10.0])  # RidgeCV 通过内置的 Alpha 参数的交叉验证来实现岭回归
regr_BR = linear_model.BayesianRidge()
regr_KR = KernelRidge(alpha=.001,kernel='rbf')
regr_RFR = RandomForestRegressor()
regr_SVR = SVR(kernel='rbf',C=100, gamma=.2)

# LinearRegression
regr_LR.fit(X_train, y_train)
y_test_pred_LR = regr_LR.predict(X_test)
y_train_pred_LR = regr_LR.predict(X_train)
print('LinearRegression:')
print('='*50)
print("RMSE: %.2f"%sqrt(mean_squared_error(y_test, y_test_pred_LR)))
print('Variance score: %.2f' % r2_score(y_test, y_test_pred_LR))
print('='*50, end='\n'*2)

# RidgeCV
regr_RCV.fit(X_train, y_train)
y_test_pred_RCV = regr_RCV.predict(X_test)
y_train_pred_RCV = regr_RCV.predict(X_train)
print('RidgeCV:')
print('='*50)
print("RMSE: %.2f"%sqrt(mean_squared_error(y_test, y_test_pred_RCV)))
print('Variance score: %.2f' % r2_score(y_test, y_test_pred_RCV))
print('='*50, end='\n'*2)

# BayesianRidge
regr_BR.fit(X_train, y_train)
y_test_pred_BR = regr_BR.predict(X_test)
y_train_pred_BR = regr_BR.predict(X_train)
print('BayesianRidge:')
print('='*50)
print("RMSE: %.2f"%sqrt(mean_squared_error(y_test, y_test_pred_BR)))
print('Variance score: %.2f' % r2_score(y_test, y_test_pred_BR))
print('='*50, end='\n'*2)

# KernelRidge
regr_KR.fit(X_train, y_train)
y_test_pred_KR = regr_KR.predict(X_test)
y_train_pred_KR = regr_KR.predict(X_train)
print('KernelRidge:')
print('='*50)
print("RMSE: %.2f"%sqrt(mean_squared_error(y_test, y_test_pred_KR)))
print('Variance score: %.2f' % r2_score(y_test, y_test_pred_KR))
print('='*50, end='\n'*2)

# RandomForestRegressor
regr_RFR.fit(X_train, y_train)
y_test_pred_RFR = regr_RFR.predict(X_test)
y_train_pred_RFR = regr_RFR.predict(X_train)
print('RandomForestRegressor:')
print('='*50)
print("RMSE: %.2f"%sqrt(mean_squared_error(y_test, y_test_pred_RFR)))
print('Variance score: %.2f' % r2_score(y_test, y_test_pred_RFR))
print('='*50, end='\n'*2)

# SVR
regr_SVR.fit(X_train, y_train)
y_test_pred_SVR = regr_SVR.predict(X_test)
y_train_pred_SVR = regr_SVR.predict(X_train)
print('SVR:')
print('='*50)
print("RMSE: %.2f"%sqrt(mean_squared_error(y_test, y_test_pred_SVR)))
print('Variance score: %.2f' % r2_score(y_test, y_test_pred_SVR))
print('='*50, end='\n'*2)


######################################## 画图 #############################################
# LinearRegression
plt.figure(figsize=(7, 7))
plt.subplot(3,2,1)
plt.scatter(y_train,y_train_pred_LR, color='black',label='TrainSet')
plt.scatter(y_test, y_test_pred_LR, color='red',label='TestSet')
plt.plot([min(y_test),max(y_test_pred_LR)],[min(y_test),max(y_test_pred_LR)])
# plt.xlabel('test')
plt.ylabel('predict')
plt.xticks()
plt.yticks()
plt.title('Energy/(eV)')
plt.text(-500,-320,'LinearRegression',fontsize=15,bbox = dict(facecolor = "r", alpha = 0.2))
# plt.text(-350,-500,"RMSE:",sqrt(mean_squared_error(y_test, y_test_pred_LR)),fontsize=10)
plt.legend()

# RidgeCV
plt.subplot(3,2,2)
plt.scatter(y_train,y_train_pred_RCV, color='black',label='TrainSet')
plt.scatter(y_test, y_test_pred_RCV, color='red',label='TestSet')
plt.plot([min(y_test),max(y_test_pred_RCV)+1],[min(y_test),max(y_test_pred_RCV)+1])
# plt.xlabel('test')
plt.ylabel('predict')
plt.xticks()
plt.yticks()
plt.title('Energy/(eV)')
plt.text(-500,-320,'RidgeCV',fontsize=15,bbox = dict(facecolor = "r", alpha = 0.2))
plt.legend()

# BayesianRidge
plt.subplot(3,2,3)
plt.scatter(y_train,y_train_pred_BR, color='black',label='TrainSet')
plt.scatter(y_test, y_test_pred_BR, color='red',label='TestSet')
plt.plot([min(y_test),max(y_test_pred_BR)+1],[min(y_test),max(y_test_pred_BR)+1])
# plt.xlabel('test')
plt.ylabel('predict')
plt.xticks()
plt.yticks()
# plt.title('Energy/(eV)')
plt.text(-500,-320,'BayesianRidge',fontsize=15,bbox = dict(facecolor = "r", alpha = 0.2))
plt.legend()

# KernelRidge
plt.subplot(3,2,4)
plt.scatter(y_train,y_train_pred_KR, color='black',label='TrainSet')
plt.scatter(y_test, y_test_pred_KR, color='red',label='TestSet')
plt.plot([min(y_test),max(y_test_pred_KR)+1],[min(y_test),max(y_test_pred_KR)+1])
# plt.xlabel('test')
plt.ylabel('predict')
plt.xticks()
plt.yticks()
# plt.title('Energy/(eV)')
plt.text(-500,-320,'KernelRidge',fontsize=15,bbox = dict(facecolor = "r", alpha = 0.2))
plt.legend()

# RandomForestRegressor
plt.subplot(3,2,5)
plt.scatter(y_train,y_train_pred_RFR, color='black',label='TrainSet')
plt.scatter(y_test, y_test_pred_RFR, color='red',label='TestSet')
plt.plot([min(y_test),max(y_test_pred_RFR)+1],[min(y_test),max(y_test_pred_RFR)+1])
plt.xlabel('test')
plt.ylabel('predict')
plt.xticks()
plt.yticks()
# plt.title('Energy/(eV)')
plt.text(-500,-320,'RandomForestRegressor',fontsize=15,bbox = dict(facecolor = "r", alpha = 0.2))
plt.legend()

# SVR
plt.subplot(3,2,6)
plt.scatter(y_train,y_train_pred_SVR, color='black',label='TrainSet')
plt.scatter(y_test, y_test_pred_SVR, color='red',label='TestSet')
plt.plot([min(y_test),max(y_test_pred_SVR)+1],[min(y_test),max(y_test_pred_SVR)+1])
plt.xlabel('test')
plt.ylabel('predict')
plt.xticks()
plt.yticks()
# plt.title('Energy/(eV)')
plt.text(-500,-320,'SVR',fontsize=15,bbox = dict(facecolor = "r", alpha = 0.2))
plt.text(-500, -100, 'colored text in axes coords',
        verticalalignment='bottom', horizontalalignment='right',
        color='green', fontsize=15)
plt.legend()

plt.show()