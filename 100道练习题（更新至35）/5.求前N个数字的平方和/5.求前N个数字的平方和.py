def sumOfSquares(num):
    # 输入数字num
    # 计算1~num的平方的和
    result=0
    for i in range(1,num+1):
        result+=(i*i)
    return result
print(sumOfSquares(3))

