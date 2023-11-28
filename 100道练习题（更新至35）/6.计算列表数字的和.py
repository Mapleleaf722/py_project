# 计算列表中所有数字的和

def sumOfList(list_:'list'):
    result=0
    for i in list_:
        result+=i
    return result

listA=[1,23,4,5,53.4,5]
listB=[17,5,3,5]
print(f'sum of {listA}:{sumOfList(listA)}')
print(f'sum of {listB}:{sumOfList(listB)}')

# python有内置函数sum()
print(sum(listA))