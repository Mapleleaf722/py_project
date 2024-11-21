# 输入:
#     原始列表: [3,5,7,9,11,13]
#     移除元素: [7,11]
# 返回:[3, 5, 9, 13]
lista=[3,5,7,9,11,13]
listb=[7,11]
def remove_elements(lista,listb):
    for i in listb:
        lista.remove(i)
    return lista
print(f'from {lista} remove {listb}, rensult:',remove_elements(lista,listb))

# 列表推导式实现
lista=[3,5,7,9,11,13]
listb=[7,11]
data=[item for item in lista if item not in listb]
print(f'from {lista} remove {listb}, rensult:',data)
