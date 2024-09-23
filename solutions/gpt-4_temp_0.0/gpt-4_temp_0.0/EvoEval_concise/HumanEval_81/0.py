
def numerical_letter_grade(grades):
    """Convert a list of GPA scores into equivalent letter grades according to the predetermined grading system. The GPA to letter grade mapping is as follows:
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

    Example:
    numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) ==> ['A+', 'B', 'C-', 'C', 'A-']
    """
    letter_grades = []
    for grade in grades:
        if grade == 4.0:
            letter_grades.append('A+')
        elif grade > 3.7:
            letter_grades.append('A')
        elif grade > 3.3:
            letter_grades.append('A-')
        elif grade > 3.0:
            letter_grades.append('B+')
        elif grade > 2.7:
            letter_grades.append('B')
        elif grade > 2.3:
            letter_grades.append('B-')
        elif grade > 2.0:
            letter_grades.append('C+')
        elif grade > 1.7:
            letter_grades.append('C')
        elif grade > 1.3:
            letter_grades.append('C-')
        elif grade > 1.0:
            letter_grades.append('D+')
        elif grade > 0.7:
            letter_grades.append('D')
        elif grade > 0.0:
            letter_grades.append('D-')
        else:
            letter_grades.append('E')
    return letter_grades