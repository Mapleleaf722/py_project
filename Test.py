def signa_sum(start, end, func):
    result = 0
    for i in range(start, end + 1):
        result += func(i)
    return result


def binary(i):
    return 2 ** i


print(signa_sum(0, 8, binary))


# def romanToInt( s: str) -> int:
#     a = ["I", "V", "X", "L", "C", "D", "M"]
#     b = [1, 5, 10, 50, 100, 500, 1000]
#     roman = {x: b[a.index(x)] for x in a}
#     str_list= list(s)
#     int_list = []
#     for i in str_list:
#         int_list.append(roman[i])
#     if str_list.index("I")<str_list.index("V")
#     print(int_list)
# romanToInt("III")

print(int('0b11111111',2))
