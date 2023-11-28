# 输入文件 :
#     三列:学号、姓名、成绩
#     列之间用逗号分割，比如”101,小张，88"
#     行之间用\n换行分割
# 输出 : 最高分、最低分、平均分
def compute_score():
    scores = []
    with open('./student_grade_input.txt', encoding='utf-8') as f:
        for line in f:
            # 去掉换行符
            line = line[:-1]
            fields = line.split(',')
            scores.append(int(fields[-1]))
    max_score = max(scores)
    min_score = min(scores)
    avg_score = round(sum(scores) / len(scores), 2)
    return max_score, min_score, avg_score


max_score, min_score, avg_score = compute_score()

print(f'max_score={max_score}, min_score={min_score}, avg_score={avg_score}')
