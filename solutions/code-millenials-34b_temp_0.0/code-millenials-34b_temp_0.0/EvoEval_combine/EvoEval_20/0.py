
def grade_and_case(s, grades):
    grade_dict = {4.0: 'A+', 3.7: 'A', 3.3: 'A-', 3.0: 'B+', 2.7: 'B', 2.3: 'B-', 2.0: 'C+', 1.7: 'C', 1.3: 'C-', 1.0: 'D+', 0.7: 'D', 0.0: 'D-', 0.0: 'E'}
    result = []
    for (name, gpa) in zip(s, grades):
        reversed_name = name.swapcase()
        letter_grade = grade_dict[gpa]
        result.append((reversed_name, letter_grade))
    return result