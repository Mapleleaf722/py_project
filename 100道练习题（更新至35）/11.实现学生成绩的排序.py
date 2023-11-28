# 学生成绩数据格式
# 复杂列表，元素是字典或者元组
# [
{'sno': 101,'sname':"小张",'sgrade':88},
{'sno': 102,'sname':"小王",'sgrade':77},
{'sno': 103,'sname':'小李','sgrade':99},
{'sno': 104,'sname':'小赵','sgrade':66}
# ]

grades=[
{'sno': 101,'sname':"小张",'sgrade':88},
{'sno': 102,'sname':"小王",'sgrade':77},
{'sno': 103,'sname':'小李','sgrade':99},
{'sno': 104,'sname':'小赵','sgrade':66}
]
# 若要降序排列，仍使用reverse参数,赋值为True
print(f'source: {grades},\nsort result: {sorted(grades,key=lambda x: x["sgrade"])}')

