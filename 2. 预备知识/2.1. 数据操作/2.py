# -*- coding = utf-8 -*-
"""
@Time : 2022/10/7 21:38
@Author : Red9th
@File : 2,3,4.py
@Software : PyCharm
"""
import tensorflow as tf

a = tf.reshape(tf.range(6), (3, 2, 1))
b = tf.reshape(tf.range(6), (1, 2, 3))

print('a', a)
print('b', b)
print(a + b)