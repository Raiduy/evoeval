
def solve_and_count(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = ''
    count = 0
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].islower():
                result += s[i].upper()
            else:
                result += s[i].lower()
        else:
            result += s[i]
    if not any((char.isalpha() for char in result)):
        result = result[::-1]
    for i in range(1, len(result), 2):
        if result[i].isupper() and result[i] in vowels:
            count += 1
    return (result, count)