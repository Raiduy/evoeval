
def grade_students(student_info, n):
    vowels = ['a', 'e', 'i', 'o', 'u']
    grades = {4.0: 'A+', 3.7: 'A', 3.3: 'A-', 3.0: 'B+', 2.7: 'B', 2.3: 'B-', 2.0: 'C+', 1.7: 'C', 1.3: 'C-', 1.0: 'D+', 0.7: 'D', 0.0: 'D-', 0.0: 'E'}
    result = []
    for student in student_info:
        name = student['name']
        gpa = student['GPA']
        consonants = sum((1 for c in name if c.lower() not in vowels))
        if consonants == n:
            grade = grades.get(gpa, 'E')
        else:
            grade = grades.get(gpa - 0.3, 'E')
        result.append({'name': name, 'grade': grade})
    return result