import re

content = """
小明上街买菜
买了1斤黄瓜花了8元;
买了2斤葡萄花了13.5元;
买了3斤白菜花了5.4元;
"""
# 要求提取 (1、黄瓜、8) 、 (2、葡萄、13.5) 、 (3、白菜、5.4)

for line in content.split('\n'):
    # *号代表前面的字符可以不出现，也可以出现一次或者多次（0次、或1次、或多次）
    # .匹配除换行符（\n、\r）之外的任何单个字符，相等于[ ^\n\r]
    # ? 等价于{0, 1}
    # ( )：用于分组和捕获子表达式。
    pattern = r'(\d)斤(.*)花了(\d+(\.\d+)?)元'
    match = re.search(pattern, line)
    if match:
        print(f'{match.group(1)}\t{match.group(2)}\t{match.group(3)}')