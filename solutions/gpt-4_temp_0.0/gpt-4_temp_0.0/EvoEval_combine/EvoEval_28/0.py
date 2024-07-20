
def grade_with_same_chars(grades: list, s0: str, s1: str):
    """
    A teacher has a special grading system where she assigns her students letter grades 
    based on their GPA according to the following table:

             GPA       |    Letter grade
              4.0                A+
            > 3.7                A 
            > 3.3                A- 
            > 3.0                B+
            > 2.7                B 
            > 2.3                B-
            > 2.0                C+
            > 1.7                C
            > 1.3                C-
            > 1.0                D+ 
            > 0.7                D 
            > 0.0                D-
              0.0                E

    However, this year she adds an extra condition: the students can only receive a grade 
    if their name (s0) and the course title (s1) have the same characters. The function 
    receives a list of GPAs and two strings (s0 and s1) and returns a list of grades 
    for the students that pass the condition, or an empty list if no student passes.

    Example:
    grade_with_same_chars([4.0, 3, 1.7, 2, 3.5], 'abcd', 'dcba') ==> ['A+', 'B', 'C-', 'C', 'A-']
    grade_with_same_chars([4.0, 3, 1.7, 2, 3.5], 'aaabcd', 'dddcba') ==> ['A+', 'B', 'C-', 'C', 'A-']
    grade_with_same_chars([4.0, 3, 1.7, 2, 3.5], 'abcd', 'dcbae') ==> []
    """
    if sorted(s0) != sorted(s1):
        return []
    grading_system = {4.0: 'A+', 3.7: 'A', 3.3: 'A-', 3.0: 'B+', 2.7: 'B', 2.3: 'B-', 2.0: 'C+', 1.7: 'C', 1.3: 'C-', 1.0: 'D+', 0.7: 'D', 0.0: 'D-', 0.0: 'E'}
    grades_assigned = []
    for gpa in grades:
        for key in sorted(grading_system.keys(), reverse=True):
            if gpa >= key:
                grades_assigned.append(grading_system[key])
                break
    return grades_assigned