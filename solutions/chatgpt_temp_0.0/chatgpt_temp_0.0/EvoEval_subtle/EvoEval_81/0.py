
def numerical_letter_grade(grades):
    grade_table = {4.0: 'A+', 3.7: 'A', 3.3: 'A-', 3.0: 'B+', 2.7: 'B', 2.3: 'B-', 2.0: 'C+', 1.7: 'C', 1.3: 'C-', 1.0: 'D+', 0.7: 'D', 0.0: 'D-'}
    sorted_grades = sorted(grades, reverse=True)
    letter_grades = [grade_table[gpa] for gpa in sorted_grades]
    return letter_grades