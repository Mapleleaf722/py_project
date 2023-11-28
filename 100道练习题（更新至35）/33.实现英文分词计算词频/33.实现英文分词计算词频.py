import pandas
import re

with open('content.txt', encoding='utf-8') as f:
    content = f.read()
    # re.split方法按照能够匹配的子串将字符串分割后返回列表
    content = re.split(r'[\s.()-?:]+', content)
print(content)
print(pandas.Series(content).value_counts()[:20])
