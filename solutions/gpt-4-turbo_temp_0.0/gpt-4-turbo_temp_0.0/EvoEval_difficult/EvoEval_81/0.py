def numerical_letter_grade_with_weightage(grades):

    def calculate_letter_grade(final_gpa):
        if final_gpa >= 4.0:
            return 'A+'
        elif final_gpa > 3.7:
            return 'A'
        elif final_gpa > 3.3:
            return 'A-'
        elif final_gpa > 3.0:
            return 'B+'
        elif final_gpa > 2.7:
            return 'B'
        elif final_gpa > 2.3:
            return 'B-'
        elif final_gpa > 2.0:
            return 'C+'
        elif final_gpa > 1.7:
            return 'C'
        elif final_gpa > 1.3:
            return 'C-'
        elif final_gpa > 1.0:
            return 'D+'
        elif final_gpa > 0.7:
            return 'D'
        elif final_gpa > 0.0:
            return 'D-'
        else:
            return 'E'
    letter_grades = []
    for (gpa, weightage) in grades:
        final_gpa = gpa * weightage
        final_gpa = min(final_gpa, 4.0)
        letter_grades.append(calculate_letter_grade(final_gpa))
    return letter_grades