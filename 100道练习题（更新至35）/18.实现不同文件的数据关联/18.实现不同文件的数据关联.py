course_teacher_map = {}
with open('course_teacher.txt', 'r+', encoding='utf-8') as teacher:
    for line in teacher:
        line = line[:-1]
        course, teacher = line.split(',')
        course_teacher_map[course] = teacher
print(course_teacher_map)
with open('course_student_grade_input.txt', encoding='utf-8') as f:
    for line in f:
        line = line[:-1]
        course, sno, sname, sgrade = line.split(',')
        teacher = course_teacher_map.get(course)
        print(course,teacher, sno, sname, sgrade)
