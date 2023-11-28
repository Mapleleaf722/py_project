def hannuota(n, x, y, z):
    """这是一个函数说明"""
    if n == 1:
        print(x, '-->', z)  # 如果只有1层，直接从x移动到z
    else:
        hannuota(n - 1, x, z, y)  # 将x上的n-1个金片移动到y
        print(x, '-->', z)  # 将最底下的金片移动到z
        hannuota(n - 1, y, x, z)  # 将y上的n-1个金片移动到z


n = int(input("输入汉诺塔的层数："))
hannuota(n, "A", 'B', 'C')
