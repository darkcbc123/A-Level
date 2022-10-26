students = {
    'student_1': [8,12,2,2,2],
    'student_2': [8,5,6,7,5],
    'student_3': [4,11,7,4,9],
    'student_4': [11,11,11,11,11],
    'student_5': [8,8,8,8,8]
}

for k, v in students.items():
    count = 0
    for i in v:
        count += i
    gpa = int(count / len(v))
    students[k] = gpa

all_gpa = []

for v in students.values():
    all_gpa.append(v)

for k, v in students.items():
    if v == max(all_gpa):
        print(f'best = {k} >>> {v}')
            
    elif v == min(all_gpa ):
        print(f'worse = {k} >>> {v}')