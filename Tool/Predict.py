from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np


######################################################
#                                                    #
#               线性回归:正规方程                    #
#                                                    #
######################################################

def predict_passer(temp, wea, passer):

    # 1.获取数据

    days = ["周五（6日）", "周六（7日）", "周日（8日）", "周一（9日）", "周二（10日）", "周三（11日）", "周四（12日）", "周五（13日）"]
    factors = ["天气", "温度", "客流"]

    lists = []

    for i, j, k in zip(temp, wea, passer):
        row = []
        row.append(i)
        row.append(j)
        row.append(k)
        lists.append(row)

    data = np.array(lists)

    data = pd.DataFrame(data, columns=factors, index=days)

    x = data[[
        "天气",
        "温度"
    ]]
    y = data["客流"]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=22)

    # 3.特征工程-标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.fit_transform(x_test)

    # 4.机器学习-线性回归
    estimator = LinearRegression()
    estimator.fit(x_train, y_train)


    # 4.模型评估
    # 4.1 预测值
    y_pre = estimator.predict(x_test)

    return round(y_pre[-1], 2)


