def hannuota(n, x, y, z):
    """这是一个函数说明"""
    if n == 1:
        print(x, '-->', z)  # 如果只有1层，直接从x移动到z
    else:
        hannuota(n - 1, x, z, y)  # 将x上的n-1个金片移动到y
        print(x, '-->', z)  # 将最底下的金片移动到z
        hannuota(n - 1, y, x, z)  # 将y上的n-1个金片移动到z


# n = int(input("输入汉诺塔的层数："))
# hannuota(n, "A", 'B', 'C')


def fib(n):
    if n == 1 or n == 2:
        return 1
    elif n <= 0:
        return "请输入正整数"
    elif n >= 2:
        return fib(n - 1) + fib(n - 2)


# print(fib(21))

def gcd(a: int, b: int):
    if a >= b >= 0:
        r = a % b
        while b != 0:
            a, b = b, a % b
        return a
    else:
        return "请输入正确的正整数！！"


print(gcd(48, 18))  # 输出: 6
print(gcd(64, 24))  # 输出: 8
print(gcd(120, 80))  # 输出: 40
