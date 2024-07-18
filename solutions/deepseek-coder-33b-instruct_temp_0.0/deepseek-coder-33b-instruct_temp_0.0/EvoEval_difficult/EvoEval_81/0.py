def numerical_letter_grade_with_weightage(grades):
    letter_grades = []
    for grade in grades:
        weighted_gpa = min(grade[0] * grade[1], 4.0)
        if weighted_gpa == 4.0:
            letter_grades.append('A+')
        elif weighted_gpa > 3.7:
            letter_grades.append('A')
        elif weighted_gpa > 3.3:
            letter_grades.append('A-')
        elif weighted_gpa > 3.0:
            letter_grades.append('B+')
        elif weighted_gpa > 2.7:
            letter_grades.append('B')
        elif weighted_gpa > 2.3:
            letter_grades.append('B-')
        elif weighted_gpa > 2.0:
            letter_grades.append('C+')
        elif weighted_gpa > 1.7:
            letter_grades.append('C')
        elif weighted_gpa > 1.3:
            letter_grades.append('C-')
        elif weighted_gpa > 1.0:
            letter_grades.append('D+')
        elif weighted_gpa > 0.7:
            letter_grades.append('D')
        elif weighted_gpa > 0.0:
            letter_grades.append('D-')
        else:
            letter_grades.append('E')
    return letter_grades