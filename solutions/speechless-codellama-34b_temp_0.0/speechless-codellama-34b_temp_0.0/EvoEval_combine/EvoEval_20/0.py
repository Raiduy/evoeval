
def grade_and_case(s, grades):
    result = []
    for i in range(len(s)):
        name = s[i]
        grade = grades[i]
        if grade == 4.0:
            letter_grade = 'A+'
        elif grade > 3.7:
            letter_grade = 'A'
        elif grade > 3.3:
            letter_grade = 'A-'
        elif grade > 3.0:
            letter_grade = 'B+'
        elif grade > 2.7:
            letter_grade = 'B'
        elif grade > 2.3:
            letter_grade = 'B-'
        elif grade > 2.0:
            letter_grade = 'C+'
        elif grade > 1.7:
            letter_grade = 'C'
        elif grade > 1.3:
            letter_grade = 'C-'
        elif grade > 1.0:
            letter_grade = 'D+'
        elif grade > 0.7:
            letter_grade = 'D'
        elif grade > 0.0:
            letter_grade = 'D-'
        else:
            letter_grade = 'E'
        reversed_name = name[::-1]
        result.append((reversed_name, letter_grade))
    return result