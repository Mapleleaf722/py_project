def course_grade_max_min_avg():
    datas = {}
    with open('course_student_grade_input.txt', encoding='utf-8') as f:
        for line in f:
            line = line[:-1]
            course, sno, name, course_grade = line.split(',')
            if course not in datas:
                datas[course] = []
            datas[course].append(int(course_grade))
    print(datas)
    for course, course_grade in datas.items():
        print(
            course,
            max(course_grade),
            min(course_grade),
            sum(course_grade) / len(course_grade)
        )


course_grade_max_min_avg()
