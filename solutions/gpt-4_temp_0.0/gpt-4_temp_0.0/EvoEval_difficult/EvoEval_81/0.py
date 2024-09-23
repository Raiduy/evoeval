def numerical_letter_grade_with_weightage(grades):
    letter_grades = []
    for grade in grades:
        weighted_grade = grade[0] * grade[1]
        if weighted_grade > 4.0:
            weighted_grade = 4.0
        if weighted_grade == 4.0:
            letter_grades.append('A+')
        elif weighted_grade > 3.7:
            letter_grades.append('A')
        elif weighted_grade > 3.3:
            letter_grades.append('A-')
        elif weighted_grade > 3.0:
            letter_grades.append('B+')
        elif weighted_grade > 2.7:
            letter_grades.append('B')
        elif weighted_grade > 2.3:
            letter_grades.append('B-')
        elif weighted_grade > 2.0:
            letter_grades.append('C+')
        elif weighted_grade > 1.7:
            letter_grades.append('C')
        elif weighted_grade > 1.3:
            letter_grades.append('C-')
        elif weighted_grade > 1.0:
            letter_grades.append('D+')
        elif weighted_grade > 0.7:
            letter_grades.append('D')
        elif weighted_grade > 0.0:
            letter_grades.append('D-')
        else:
            letter_grades.append('E')
    return letter_grades