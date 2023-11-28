import re

# compile 函数用于编译正则表达式，生成一个 Pattern 对象
pattern = re.compile(r"[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-z]{2,4}")
with open('web_article.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    # compile()与findall()一起使用，返回一个列表
    results = pattern.findall(content)
for result in results:
    print(result)
