
def hex_grade_calculator(grades):
    prime_grades = ['D', 'B', '7', '5', '3']
    grade_ranges = [(4.0, 'F'), (3.7, 'E'), (3.3, 'D'), (3.0, 'C'), (2.7, 'B'), (2.3, 'A'), (2.0, '9'), (1.7, '8'), (1.3, '7'), (1.0, '6'), (0.7, '5'), (0.0, '4'), (0.0, '3')]
    prime_grade_count = 0
    for grade in grades:
        for i in range(len(grade_ranges)):
            if grade >= grade_ranges[i][0]:
                if grade_ranges[i][1] in prime_grades:
                    prime_grade_count += 1
                break
    return prime_grade_count