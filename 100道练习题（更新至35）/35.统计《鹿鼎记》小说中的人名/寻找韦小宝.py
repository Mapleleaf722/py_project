import re

with open('《鹿鼎记》.txt', encoding='utf-8') as f:
    content = f.read()
    print(len(re.findall('韦小宝', content)))
