import copy

list_1 = [1, [22, 33, 44], (5, 6, 7), {"name": "Sarah"}]
list_2 = copy.deepcopy(list_1)
print(id(list_1[1]), id(list_1[2]))
print(id(list_2[1]))
