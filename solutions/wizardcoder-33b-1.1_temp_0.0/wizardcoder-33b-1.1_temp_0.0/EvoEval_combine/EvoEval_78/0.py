
def solve_and_count(s):
    vowels = 'AEIOU'
    s = list(s)
    has_letter = False
    for i in range(len(s)):
        if s[i].isalpha():
            has_letter = True
            s[i] = s[i].lower() if s[i].isupper() else s[i].upper()
    if not has_letter:
        s = s[::-1]
    count = sum((1 for i in range(0, len(s), 2) if s[i].isupper() and s[i] in vowels))
    return (''.join(s), count)