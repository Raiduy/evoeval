
def grade_students(student_info, n):
    """You are a programming teacher and the semester is ending. You have a list of dictionaries, each containing 
    the name and GPA of a student. Additionally, you have a special grading system. Each student's name contributes 
    to their final grade based on the number of consonants in their name. If their name contains exactly n consonants,
    their final grade gets bumped up one level according to the grading scale below:

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

    Write a function that takes the list of students and the number n and returns a list of dictionaries with each 
    student's name and their final letter grade. If the student name does not contain exactly n consonants, the grade 
    is not bumped up.

    Example:
    grade_students([{'name': 'Alice', 'GPA': 3.0}, {'name': 'Bob', 'GPA': 2.3}, {'name': 'Charlie', 'GPA': 3.3}], 2) 
    ==> [{'name': 'Alice', 'grade': 'B+'}, {'name': 'Bob', 'grade': 'B-'}, {'name': 'Charlie', 'grade': 'B+'}]
    """

    def count_consonants(name):
        return sum((1 for char in name.lower() if char in 'bcdfghjklmnpqrstvwxyz'))

    def get_grade(gpa):
        if gpa == 4.0:
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

    def bump_grade(grade):
        if grade == 'A+':
            return 'A+'
        elif grade == 'A':
            return 'A+'
        elif grade == 'A-':
            return 'A'
        elif grade == 'B+':
            return 'A-'
        elif grade == 'B':
            return 'B+'
        elif grade == 'B-':
            return 'B'
        elif grade == 'C+':
            return 'B-'
        elif grade == 'C':
            return 'C+'
        elif grade == 'C-':
            return 'C'
        elif grade == 'D+':
            return 'C-'
        elif grade == 'D':
            return 'D+'
        elif grade == 'D-':
            return 'D'
        else:
            return 'D+'
    for student in student_info:
        student['grade'] = get_grade(student['GPA'])
        if count_consonants(student['name']) == n:
            student['grade'] = bump_grade(student['grade'])
    return student_info