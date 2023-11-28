# 输入文件
#     三列:学号、姓名、成绩
#     列之间用逗号分割,比如:"101, 小张,88"
#     行之间用\n换行分割
# 处理:读取文件，按成绩倒序排列
# 输出:排序后的三列数据

def read_file():
    result = []
    with open('./student_grade_input.txt', encoding='utf-8') as f:
        # 读取的文件以行为单位
        for line in f:
            line = line[:-1]
            # split()函数返回一个列表
            result.append(line.split(','))
    return result


# 读取文件
datas = read_file()
print(datas)


# 排序数据
def sort_grades(datas):
    return sorted(datas, key=lambda x: x[2], reverse=True)


datas = sort_grades(datas)


# 写出文件
def write_file(datas):
    with open('./student_grade_output.txt', 'w', encoding='utf-8') as f:
        for i in datas:
            f.write(",".join(i) + '\n')


write_file(datas)
