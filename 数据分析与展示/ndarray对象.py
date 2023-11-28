# 例: 计算 A**2+B**2，其中，A和B是一维数组

# 不使用numpy
def pySum():
    a = [0, 1, 2, 3, 4]
    b = [9, 8, 7, 6, 5]
    c = []
    for i in range(len(a)):
        c.append(a[i] ** 2 + b[i] ** 2)
    return c


print(f'不使用numpy的结果:{pySum()}，类型为:{type(pySum())}')

# 使用numpy,无须使用循环
import numpy as np


def pySum_():
    a = np.array([0, 1, 2, 3, 4])
    b = np.array([9, 8, 7, 6, 5])
    c = a ** 2 + b ** 2
    return c


print(f'使用numpy的结果:{pySum_()}，类型为:{type(pySum_())}')
