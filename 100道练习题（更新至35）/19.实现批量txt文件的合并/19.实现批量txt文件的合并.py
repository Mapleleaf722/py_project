# python读取文件的两个方法
# 1 按行读取
# 2 一次读取所有内容到一个字符串
import os

data_dir = './many_texts'
contents = []
# os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字
for file in os.listdir(data_dir):
    file_path = f'{data_dir}/{file}'
    if os.path.isfile(file_path) and file.endswith('.txt'):
        with open(file_path, encoding='utf-8') as f:
            contents.append(f.read())
final_content = '\n'.join(contents)
with open('./many_texts/many_texts.txt', 'w', encoding='utf-8') as f:
    f.write(final_content)
