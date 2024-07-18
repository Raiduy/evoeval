
def hex_grade_calculator(grades):
    gpa_to_hex = [(4.0, 'F'), (3.7, 'E'), (3.3, 'D'), (3.0, 'C'), (2.7, 'B'), (2.3, 'A'), (2.0, '9'), (1.7, '8'), (1.3, '7'), (1.0, '6'), (0.7, '5'), (0.0, '4'), (0.0, '3')]
    prime_hex_grades = ['D', 'B', '7', '5', '3']

    def find_hex_grade(gpa):
        for (threshold, hex_grade) in gpa_to_hex:
            if gpa > threshold:
                return hex_grade
        return '3'
    hex_grades = [find_hex_grade(gpa) for gpa in grades]
    prime_grade_count = sum((1 for grade in hex_grades if grade in prime_hex_grades))
    return prime_grade_count