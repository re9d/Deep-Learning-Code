# -*- coding = utf-8 -*-
"""
@Time : 2022/10/11 16:36
@Author : Red9th
@File : 2,3,4.py
@Software : PyCharm
"""
"""
Exercise 2
max(P(A), P(B)) <= P(A ∪ B) <= P(A) + P(B)
0 <= P(A ∩ B) <= min(P(A), P(B))
"""

"""
Exercise 3
P(AB) = P(B | A)P(A)
P(BC) = P(C | B)P(B)
P(ABC) = P(A)P(B | A)P(C | AB)
根据马尔可夫链：(A->B->C)
P(C | AB) = P(C | B)
所以：
P(ABC) = P(A)P(B | A)P(C | B)
"""

"""
Exercise 4
原因是如果进行两次第一种测试，两次测试没有条件独立性，不能使用上面的公式进行计算，而且两次测试结果大概率相同，效果并不好。
计算最后发现确实非常相近。
"""