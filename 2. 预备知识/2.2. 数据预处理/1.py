# -*- coding = utf-8 -*-
"""
@Time : 2022/10/7 21:52
@Author : Red9th
@File : 5.py
@Software : PyCharm
"""
import os
import tensorflow as tf
import pandas as pd

os.makedirs(os.path.join('.', 'data'), exist_ok=True)
data_file = os.path.join('.', 'data', 'house_tiny.csv')
with open(data_file, 'w') as f:
    f.write('NumRooms,Alley,Size,Price\n')  # 列名
    f.write('NA,Pave,NA,127500\n')  # 每行表示一个数据样本
    f.write('2,NA,NA,106000\n')
    f.write('4,NA,NA,178100\n')
    f.write('NA,NA,NA,160000\n')
    f.write('NA,NA,NA,140130\n')
    f.write('3,NA,NA,130000\n')
    f.write('3,Pave,NA,140100\n')
    f.write('6,NA,NA,192130\n')
    f.write('NA,NA,120,151210\n')

data = pd.read_csv(data_file) # 读数据
print(data)

# 1. 删除缺失值最多的列
# isna().sum(): 求每一列的缺失值的个数
data = data.iloc[:, data.isna().sum().values < data.isna().sum().max()]
print(data)

inputs, outputs = data.iloc[:, 0:2], data.iloc[:, 2]

# 处理缺失值
inputs = inputs.fillna(inputs.mean()) # Nan填充为均值
print(inputs)
inputs = pd.get_dummies(inputs, dummy_na=True) # Alley只有两种类型，被转化为0和1
print(inputs)

# 2. 转换为张量格式（inputs和outputs中的所有条目都是数值类型的前提下）
X, y = tf.constant(inputs.values), tf.constant(outputs.values)
print(X, y)