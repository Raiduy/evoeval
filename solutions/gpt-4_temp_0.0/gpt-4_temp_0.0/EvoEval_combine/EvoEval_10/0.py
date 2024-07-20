
def class_grades_with_flip(name_grade_list):
    """A teacher has to give the grades to students. The teacher has a list of students with their GPAs.
    The teacher wants to convert these GPAs into letter grades. However, due to an administrative error, 
    some students' names have been input in the wrong case (all caps or all lowercase). 
    To fix this, their names need to be converted to proper case i.e., only the first letter of the name 
    should be in uppercase and the rest in lowercase.

    Additionally, the teacher has her own algorithm for grading. Write a function that will output a list
    of tuples where each tuple contains the student's name in proper case and the corresponding letter grade 
    using the following table:
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
    class_grades_with_flip([('JOHN', 4.0), ('sarah', 3.0), ('ALICE', 1.7), ('BOB', 2.0), ('linda', 3.5)]) 
    ==> [('John', 'A+'), ('Sarah', 'B'), ('Alice', 'C-'), ('Bob', 'C'), ('Linda', 'A-')]
    """
    grading_scale = [(4.0, 'A+'), (3.7, 'A'), (3.3, 'A-'), (3.0, 'B+'), (2.7, 'B'), (2.3, 'B-'), (2.0, 'C+'), (1.7, 'C'), (1.3, 'C-'), (1.0, 'D+'), (0.7, 'D'), (0.0, 'D-'), (-1, 'E')]
    result = []
    for (name, grade) in name_grade_list:
        name = name.capitalize()
        for (gpa, letter_grade) in grading_scale:
            if grade >= gpa:
                result.append((name, letter_grade))
                break
    return result