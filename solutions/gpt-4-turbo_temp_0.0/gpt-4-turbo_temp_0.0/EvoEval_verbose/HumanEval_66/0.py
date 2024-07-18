
def digitSum(s):
    sum_of_digits = 0
    for char in s:
        if char.isupper():
            sum_of_digits += ord(char)
    return sum_of_digits