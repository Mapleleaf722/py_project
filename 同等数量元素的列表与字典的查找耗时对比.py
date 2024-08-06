# 同等数量元素的列表与字典的查找耗时对比
import time

ls_1 = list(range(100000))
ls_2 = list(range(1000)) + [-10] * 500
start_time = time.time()
count = 0
for i in ls_1:
    if i in ls_2:
        count += 1
end_time = time.time()
print(f"查找了{len(ls_2)}个元素，在ls_1中有{count}个，共耗时{end_time - start_time}秒")
dt_1 = {i: 1 for i in range(100000)}
start_time = time.time()
count = 0
for i in ls_2:
    try:
        dt_1[i]
    except:
        pass
    else:
        count += 1
end_time = time.time()
print(f"查找了{len(ls_2)}个元素，在dt_1中有{count}个，共耗时{end_time - start_time}秒")
