
def solve_and_count(s):
    vowels = 'AEIOU'
    result = ''
    count = 0
    has_letter = False
    for i in range(len(s)):
        if s[i].isalpha():
            has_letter = True
            if s[i].islower():
                result += s[i].upper()
                if i % 2 == 0 and s[i].upper() in vowels:
                    count += 1
            else:
                result += s[i].lower()
                if i % 2 == 0 and s[i].lower() in vowels:
                    count += 1
        else:
            result += s[i]
    if not has_letter:
        result = s[::-1]
    return (result, count)