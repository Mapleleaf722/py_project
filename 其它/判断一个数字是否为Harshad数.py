# 如果一个数字可以被它的数字之和整除，那么它就是一个Harshad数
def is_harshad(num):
    # 在此处编写你的代码
    str_num = str(num)
    sum_num = 0
    for i in range(len(str_num)):
        sum_num += int(str_num[i])
    if num % sum_num == 0:
        return True
    else:
        return False


# 获取用户输入
num = int(input())

# 显示输出
print(is_harshad(num))
