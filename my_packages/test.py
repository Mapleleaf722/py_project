import os

# os.path.exists() 判断路径(文件或目录)是否存在
# 存在的话就返回True,不存在就返回False
print(os.path.exists(r"D:\Python\py25\py25.py"))
# os.path.isfile() 判断是否存在文件
print(os.path.isfile(r"D:\Python\py25\py25.py"))
# os.path.isdir() 判断目录是否存在
print(os.path.isdir(r"D:\Python\py25"))
# os.path.abs() 获取当前路径下的绝对路径
print(os.path.abspath("1.py"))

