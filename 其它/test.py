def addTwoNumbers(l1: list, l2: list) -> list:
    num1, num2 = 0, 0
    for i in range(0, len(l1)):
        num1 += l1[i] * 10 ** (len(l1) - i)
    for j in range(0, len(l2)):
        num1 += l1[j] * 10 ** (len(l2) - j)
    num3 = num1 + num2
    result = list(str(num3))
    result.reverse()
    return result


print(addTwoNumbers([2, 4, 3], [5, 6, 4]))
