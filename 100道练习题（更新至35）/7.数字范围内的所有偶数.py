# 输入开始和结束值（不包含），得到所有偶数
# 输入：begin=4,end=15
# 返回：[4,6,8,10,12,14]

def allEven(start,end_):
    result=[]
    for i in range(start,end_):
        if i%2==0:
            result.append(i)
    return result

print(allEven(4,15))

# 列表推导式的方式实现：
data=[i for i in range(4,15) if i%2==0]
print(data)
