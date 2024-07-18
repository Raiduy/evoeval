
def numerical_letter_grade(grades):
    letter_grades = []
    for gpa in grades:
        if gpa == 4.0:
            grade = 'A+'
        elif gpa > 3.7:
            grade = 'A'
        elif gpa > 3.3:
            grade = 'A-'
        elif gpa > 3.0:
            grade = 'B+'
        elif gpa > 2.7:
            grade = 'B'
        elif gpa > 2.3:
            grade = 'B-'
        elif gpa > 2.0:
            grade = 'C+'
        elif gpa > 1.7:
            grade = 'C'
        elif gpa > 1.3:
            grade = 'C-'
        elif gpa > 1.0:
            grade = 'D+'
        elif gpa > 0.7:
            grade = 'D'
        elif gpa > 0.0:
            grade = 'D-'
        else:
            grade = 'E'
        letter_grades.append(grade)
    return letter_grades