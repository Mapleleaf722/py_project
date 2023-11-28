import jieba.posseg as posseg
import pandas as pd

with open("《鹿鼎记》.txt", encoding='utf-8') as f:
    content = f.read()
names = []
for word, flag in posseg.cut(content):
    if flag == 'nr':
        names.append(word)

print(pd.Series(names).value_counts()[:20])
