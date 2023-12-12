# 计算A^2+B^3,A、B是一维数组
import numpy as np

A = [0, 1, 2, 3, 4]
B = [9, 8, 7, 6, 5]


def py_sum(a, b):
    c = []
    for i in range(len(a)):
        c.append(a[i] ** 2 + b[i] ** 3)
    return c


print(py_sum(A, B))


# 使用numpy，不使用循环
def np_sum(a, b):
    a = np.array(a)
    b = np.array(b)
    c = a ** 2 + b ** 3
    return c


print(np_sum(A, B))
print(type(np_sum(A, B)))
