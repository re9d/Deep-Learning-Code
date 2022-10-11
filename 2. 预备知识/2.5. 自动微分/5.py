# -*- coding = utf-8 -*-
"""
@Time : 2022/10/10 20:34
@Author : Red9th
@File : 5.py
@Software : PyCharm
"""
import tensorflow as tf
import numpy as np
from d2l import tensorflow as d2l

x = tf.range(-4, 4, 0.01)
x = tf.Variable(x) # 存储梯度值

with tf.GradientTape() as t:
    y = tf.sin(x)
dy_dx = t.gradient(y, x)

x = np.array(x)
y = np.array(y)
dy_dx = np.array(dy_dx)

d2l.plot(x, [y, dy_dx], 'x', 'y', legend=['y=sin(x)', 'y=sin\'(x)'])