# 输入半径，返回圆的面积
# 结果保留两位小数
import math
def areaOfCircle(r):
    return round(math.pi * r * r,2)


print(areaOfCircle(2))
print(areaOfCircle(3.14))
print(areaOfCircle(6.78))