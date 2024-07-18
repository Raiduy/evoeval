
def grade_and_case(s, grades):

    def reverse_case(name):
        return name.swapcase()

    def assign_grade(gpa):
        if gpa >= 4.0:
            return 'A+'
        elif gpa > 3.7:
            return 'A'
        elif gpa > 3.3:
            return 'A-'
        elif gpa > 3.0:
            return 'B+'
        elif gpa > 2.7:
            return 'B'
        elif gpa > 2.3:
            return 'B-'
        elif gpa > 2.0:
            return 'C+'
        elif gpa > 1.7:
            return 'C'
        elif gpa > 1.3:
            return 'C-'
        elif gpa > 1.0:
            return 'D+'
        elif gpa > 0.7:
            return 'D'
        elif gpa > 0.0:
            return 'D-'
        else:
            return 'E'
    result = []
    for i in range(len(s)):
        name = reverse_case(s[i])
        grade = assign_grade(grades[i])
        result.append((name, grade))
    return result