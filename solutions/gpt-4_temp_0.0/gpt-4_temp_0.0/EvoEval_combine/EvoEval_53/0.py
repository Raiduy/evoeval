
def hex_grade_calculator(grades):
    prime_grades = ['D', 'B', '7', '5', '3']
    hex_grades = []
    for grade in grades:
        if grade == 4.0:
            hex_grades.append('F')
        elif grade > 3.7:
            hex_grades.append('E')
        elif grade > 3.3:
            hex_grades.append('D')
        elif grade > 3.0:
            hex_grades.append('C')
        elif grade > 2.7:
            hex_grades.append('B')
        elif grade > 2.3:
            hex_grades.append('A')
        elif grade > 2.0:
            hex_grades.append('9')
        elif grade > 1.7:
            hex_grades.append('8')
        elif grade > 1.3:
            hex_grades.append('7')
        elif grade > 1.0:
            hex_grades.append('6')
        elif grade > 0.7:
            hex_grades.append('5')
        elif grade > 0.0:
            hex_grades.append('4')
        else:
            hex_grades.append('3')
    return len([grade for grade in hex_grades if grade in prime_grades])