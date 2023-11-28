import numpy as np

a = np.array([[0, 1, 2, 3, 4], [9, 8, 7, 6, 5]])
print(a)
print(f'a.ndim,秩，即轴的数量或维度的数量: {a.ndim}')
print(f'a.shape,ndarray对象的尺度，对于矩阵，n行m列：{a.shape}')
print(f'a.size,ndarray对象元素的个数，相当于.shape中n*m的值：{a.size}')
print(f'a.dtype,ndarray对象的元素类型：{a.dtype}')
print(f'a.itemsize,ndarray对象中每个元素的大小，以字节为单位：{a.itemsize}')
