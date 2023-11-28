# 输入，包含重复元素的原始列表:[10, 20.统计每个兴趣的学生人数,30,10,20.统计每个兴趣的学生人数]
# 返回:[10,20.统计每个兴趣的学生人数, 30]
list1 = [10, 20, 30, 10, 20]


def get_unique_list(lista):
    result = []
    for i in lista:
        if i not in result:
            result.append(i)
    return result


print(f'source list {list1},unique list:', get_unique_list(list1))

# 利用集合不包含重复元素的特性实现
result = list(set(list1))
print(f'source list {list1},unique list:', result)
