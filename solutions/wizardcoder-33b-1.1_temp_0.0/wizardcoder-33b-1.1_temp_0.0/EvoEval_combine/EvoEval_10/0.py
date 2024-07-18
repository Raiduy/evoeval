
def class_grades_with_flip(name_grade_list):

    def convert_to_proper_case(name):
        return name.capitalize()

    def convert_to_letter_grade(gpa):
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
        elif gpa >= 0.0:
            return 'D-'
        else:
            return 'E'
    return [(convert_to_proper_case(name), convert_to_letter_grade(gpa)) for (name, gpa) in name_grade_list]