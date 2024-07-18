
def grade_students(student_info, n):

    def get_grade(gpa):
        if gpa >= 4.0:
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

    def bump_grade(grade):
        grades = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'E']
        if grade in grades and grade != 'A+':
            return grades[grades.index(grade) - 1]
        return grade

    def count_consonants(name):
        consonants = 'bcdfghjklmnpqrstvwxyz'
        return sum((1 for char in name.lower() if char in consonants))
    result = []
    for student in student_info:
        name = student['name']
        gpa = student['GPA']
        grade = get_grade(gpa)
        if count_consonants(name) == n:
            grade = bump_grade(grade)
        result.append({'name': name, 'grade': grade})
    return result