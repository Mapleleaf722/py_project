datas = {}
with open('student_like.txt', encoding='utf-8') as f:
    for line in f:
        line = line[:-1]
        likes = line.split(' ')[1]
        student = line.split(' ')[0]
        # print(line.split(' '))
        for i in likes.split('，'):
            if i not in datas.keys():
                datas[i] = []
            datas[i].append(student)

for k, v in datas.items():
    print(f'{k}: {len(v)}人')
