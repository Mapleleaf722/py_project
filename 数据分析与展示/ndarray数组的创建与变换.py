import numpy as np

a = np.arange(10)
print(a)
b = np.ones((2, 3, 4))
print(b)
c = np.zeros((5, 5))
print(c)
d = np.full((6, 6), 666)
print(d)
e = np.eye(7)
print(e)

print(np.ones_like(c))
