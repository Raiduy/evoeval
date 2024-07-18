def numerical_letter_grade_with_weightage(grades):
    letter_grades = []
    for (gpa, weightage) in grades:
        final_gpa = gpa * weightage
        if final_gpa > 4.0:
            final_gpa = 4.0
        if final_gpa >= 3.7:
            letter_grades.append('A+')
        elif final_gpa >= 3.3:
            letter_grades.append('A')
        elif final_gpa >= 3.0:
            letter_grades.append('A-')
        elif final_gpa >= 2.7:
            letter_grades.append('B+')
        elif final_gpa >= 2.3:
            letter_grades.append('B')
        elif final_gpa >= 2.0:
            letter_grades.append('B-')
        elif final_gpa >= 1.7:
            letter_grades.append('C+')
        elif final_gpa >= 1.3:
            letter_grades.append('C')
        elif final_gpa >= 1.0:
            letter_grades.append('C-')
        elif final_gpa >= 0.7:
            letter_grades.append('D+')
        elif final_gpa >= 0.0:
            letter_grades.append('D')
        else:
            letter_grades.append('E')
    return letter_grades