import os
import shutil

dir_ = './arrange_dir'

for file in os.listdir(dir_):
    # 获取文件后缀
    suffix = os.path.splitext(file)[1]
    suffix = suffix[1:]
    # 创建目录文件
    if not os.path.isdir(f'{dir_}/{suffix}'):
        os.mkdir(f'{dir_}/{suffix}')
    source_path = f'{dir_}/{file}'
    target_path = f'{dir_}/{suffix}/{file}'
    shutil.move(source_path, target_path)
