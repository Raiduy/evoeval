
def hex_grade_calculator(grades):
    prime_grades = ['D', 'B', '7', '5', '3']
    count = 0
    for grade in grades:
        if grade == 4.0:
            count += 1
        elif grade > 3.7:
            count += 1
        elif grade > 3.3:
            count += 1
        elif grade > 3.0:
            count += 1
        elif grade > 2.7:
            count += 1
        elif grade > 2.3:
            count += 1
        elif grade > 2.0:
            count += 1
        elif grade > 1.7:
            count += 1
        elif grade > 1.3:
            count += 1
        elif grade > 1.0:
            count += 1
        elif grade > 0.7:
            count += 1
        elif grade > 0.0:
            count += 1
    return count