import os

print(os.path.getsize("10.怎样对简单列表进行排序.py"))

sum_size = 0
# 列出当前目录下的文件
for file in os.listdir("."):
    if os.path.isfile(file):
        sum_size += os.path.getsize(file)
print(sum_size / 1000)
