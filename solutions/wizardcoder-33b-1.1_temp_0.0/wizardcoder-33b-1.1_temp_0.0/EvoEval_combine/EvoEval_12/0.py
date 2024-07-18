
def grade_students(student_info, n):

    def count_consonants(name):
        return sum((1 for c in name if c.lower() in 'bcdfghjklmnpqrstvwxyz'))

    def get_grade(gpa):
        if gpa == 4.0:
            return 'A+'
        elif gpa > 3.7:
            return 'A'
        elif gpa > 3.3:
            return 'A-'
        elif gpa > 3.0:
            return 'B+'
        elif gpa > 2.7:
            return 'B'
        elif gpa > 2.3:
            return 'B-'
        elif gpa > 2.0:
            return 'C+'
        elif gpa > 1.7:
            return 'C'
        elif gpa > 1.3:
            return 'C-'
        elif gpa > 1.0:
            return 'D+'
        elif gpa > 0.7:
            return 'D'
        elif gpa > 0.0:
            return 'D-'
        else:
            return 'E'
    result = []
    for student in student_info:
        if count_consonants(student['name']) == n:
            student['GPA'] += 0.3
            if student['GPA'] > 4.0:
                student['GPA'] = 4.0
            student['grade'] = get_grade(student['GPA'])
        else:
            student['grade'] = get_grade(student['GPA'])
        result.append({'name': student['name'], 'grade': student['grade']})
    return result