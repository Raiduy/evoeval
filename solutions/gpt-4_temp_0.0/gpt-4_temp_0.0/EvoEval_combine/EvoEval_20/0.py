
def grade_and_case(s, grades):
    result = []
    for i in range(len(s)):
        name = s[i].swapcase()
        if grades[i] == 4.0:
            grade = 'A+'
        elif grades[i] > 3.7:
            grade = 'A'
        elif grades[i] > 3.3:
            grade = 'A-'
        elif grades[i] > 3.0:
            grade = 'B+'
        elif grades[i] > 2.7:
            grade = 'B'
        elif grades[i] > 2.3:
            grade = 'B-'
        elif grades[i] > 2.0:
            grade = 'C+'
        elif grades[i] > 1.7:
            grade = 'C'
        elif grades[i] > 1.3:
            grade = 'C-'
        elif grades[i] > 1.0:
            grade = 'D+'
        elif grades[i] > 0.7:
            grade = 'D'
        elif grades[i] > 0.0:
            grade = 'D-'
        else:
            grade = 'E'
        result.append((name, grade))
    return result