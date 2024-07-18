
def class_grades_with_flip(name_grade_list):

    def get_letter_grade(gpa):
        if gpa >= 4.0:
            return 'A+'
        elif gpa >= 3.7:
            return 'A'
        elif gpa >= 3.3:
            return 'A-'
        elif gpa >= 3.0:
            return 'B+'
        elif gpa >= 2.7:
            return 'B'
        elif gpa >= 2.3:
            return 'B-'
        elif gpa >= 2.0:
            return 'C+'
        elif gpa >= 1.7:
            return 'C'
        elif gpa >= 1.3:
            return 'C-'
        elif gpa >= 1.0:
            return 'D+'
        elif gpa >= 0.7:
            return 'D'
        else:
            return 'D-'
    graded_students = []
    for (name, gpa) in name_grade_list:
        proper_case_name = name.capitalize()
        letter_grade = get_letter_grade(gpa)
        graded_students.append((proper_case_name, letter_grade))
    return graded_students