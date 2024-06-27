# 一个正整数的阶乘（factorial）是所有小于及等于该数的正整数的积
# 0的阶乘为1
# 自然数n的阶乘写作n!

def factorial(number):
    result = 1
    while number > 0:
        result *= number
        number -= 1
    return result


print('3的阶乘=', factorial(3))
print('6的阶乘=', factorial(6))
print('100的阶乘=', factorial(100))
