
def numerical_letter_grade(grades):
    """
    This function is designed to solve the problem of converting a list of numerical Grade Point Average (GPA) scores into corresponding letter grades, according to a pre-defined grading table. It is especially useful for teachers who are at the end of the semester and need to finalize students' letter grades based on their GPA.

    The function takes in a list of GPAs (which are floating point numbers) for a set of students as the only argument. The GPAs are expected to be between 0.0 and 4.0 (inclusive). The function uses the following grading table to perform the conversion:

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

    For example, if a student has a GPA of 3.5, his/her letter grade would be 'A-', as per the table.

    The function returns a list containing the letter grades corresponding to the input GPAs, in the same order as the input.

    Here is an example to illustrate the usage of the function:

    Example:
    numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) 
    The above function call would return: ['A+', 'B', 'C-', 'C', 'A-']
    This indicates that a GPA of 4.0 corresponds to 'A+', 3 to 'B', 1.7 to 'C-', 2 to 'C', and 3.5 to 'A-'.
    """
    letter_grades = []
    for gpa in grades:
        if gpa == 4.0:
            letter_grades.append('A+')
        elif gpa > 3.7:
            letter_grades.append('A')
        elif gpa > 3.3:
            letter_grades.append('A-')
        elif gpa > 3.0:
            letter_grades.append('B+')
        elif gpa > 2.7:
            letter_grades.append('B')
        elif gpa > 2.3:
            letter_grades.append('B-')
        elif gpa > 2.0:
            letter_grades.append('C+')
        elif gpa > 1.7:
            letter_grades.append('C')
        elif gpa > 1.3:
            letter_grades.append('C-')
        elif gpa > 1.0:
            letter_grades.append('D+')
        elif gpa > 0.7:
            letter_grades.append('D')
        elif gpa > 0.0:
            letter_grades.append('D-')
        else:
            letter_grades.append('E')
    return letter_grades