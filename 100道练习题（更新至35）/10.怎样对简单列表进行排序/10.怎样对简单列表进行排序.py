# 怎样对简单列表排序?
#     简单列表:元素类型不是复合类型(列表/元组/字典)
#     形式1: [20.统计每个兴趣的学生人数,50,10,40,30]
#     形式2: ['bb','ee','aa','dd','cc']
# 知识点:
#     怎样原地排序? 怎样不改变原列表排序?
#     怎样指定是升序还是降序排序?

list1=[20,50,10,40,30]
list2=['bb','ee','aa','dd','cc']
# 原地排序——更改原列表排序
list1.sort()
print(list1)
# 不改变原列表排序
print(sorted(list2))
print(list2)
# 升序改降序（前面两个函数sort和sorted默认都是升序）
list1.sort(reverse=True)
print(list1)
print(sorted(list2,reverse=True))
