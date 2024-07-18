
def hex_grade_calculator(grades):
    prime_grades = ['D', 'B', '7', '5', '3']
    count = 0
    for gpa in grades:
        if gpa >= 4.0:
            grade = 'F'
        elif gpa > 3.7:
            grade = 'E'
        elif gpa > 3.3:
            grade = 'D'
        elif gpa > 3.0:
            grade = 'C'
        elif gpa > 2.7:
            grade = 'B'
        elif gpa > 2.3:
            grade = 'A'
        elif gpa > 2.0:
            grade = '9'
        elif gpa > 1.7:
            grade = '8'
        elif gpa > 1.3:
            grade = '7'
        elif gpa > 1.0:
            grade = '6'
        elif gpa > 0.7:
            grade = '5'
        elif gpa > 0.0:
            grade = '4'
        else:
            grade = '3'
        if grade in prime_grades:
            count += 1
    return count