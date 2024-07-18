
def grade_with_same_chars(grades: list, s0: str, s1: str):
    grading_system = {4.0: 'A+', 3.7: 'A', 3.3: 'A-', 3.0: 'B+', 2.7: 'B', 2.3: 'B-', 2.0: 'C+', 1.7: 'C', 1.3: 'C-', 1.0: 'D+', 0.7: 'D', 0.0: 'D-', 0.0: 'E'}
    if set(s0) != set(s1):
        return []
    assigned_grades = []
    for gpa in grades:
        for (grade_gpa, grade) in grading_system.items():
            if gpa >= grade_gpa:
                assigned_grades.append(grade)
                break
    return assigned_grades