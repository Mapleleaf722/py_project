contents = """
白日依2021/05/26山尽，黄河入2021.05.27海流。
欲穷05-28-2020千里目，更上5/29/2020一层楼。
"""
# 目标:2021-05-28
import re

contents = re.sub(r'(\d{4})/(\d{2})/(\d{2})', r'\1-\2-\3', contents)
contents = re.sub(r'(\d{4})\.(\d{2})\.(\d{2})', r'\1-\2-\3', contents)
contents = re.sub(r'(\d{2})-(\d{2})-(\d{4})', r'\3-\1-\2', contents)
contents = re.sub(r'(\d)/(\d{2})/(\d{4})', r'\3-0\1-\2', contents)

print(contents)
