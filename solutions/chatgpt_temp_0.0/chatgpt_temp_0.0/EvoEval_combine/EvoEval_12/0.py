
def grade_students(student_info, n):
    grades = {4.0: 'A+', 3.7: 'A', 3.3: 'A-', 3.0: 'B+', 2.7: 'B', 2.3: 'B-', 2.0: 'C+', 1.7: 'C', 1.3: 'C-', 1.0: 'D+', 0.7: 'D', 0.0: 'D-', -1.0: 'E'}

    def count_consonants(name):
        consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
        return sum((1 for char in name if char in consonants))
    result = []
    for student in student_info:
        name = student['name']
        gpa = student['GPA']
        consonant_count = count_consonants(name)
        if consonant_count == n:
            gpa = min(4.0, gpa + 0.3)
        grade = grades[gpa]
        result.append({'name': name, 'grade': grade})
    return result