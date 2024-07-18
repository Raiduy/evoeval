
def hex_grade_calculator(grades):
    prime_grades = {'D', 'B', '7', '5', '3'}
    decimal_grades = {4.0: 'F', 3.7: 'E', 3.3: 'D', 3.0: 'C', 2.7: 'B', 2.3: 'A', 2.0: '9', 1.7: '8', 1.3: '7', 1.0: '6', 0.7: '5', 0.0: '4'}
    count = 0
    for gpa in grades:
        for key in decimal_grades:
            if gpa >= key:
                if decimal_grades[key] in prime_grades:
                    count += 1
                break
    return count