# -*- coding = utf-8 -*-
"""
@Time : 2022/10/7 21:39
@Author : Red9th
@File : 1.py
@Software : PyCharm
"""
import tensorflow as tf

X = tf.reshape(tf.range(12, dtype=tf.float32), (3, 4))
Y = tf.constant([[2.0, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])

print(X > Y)
print(X < Y)