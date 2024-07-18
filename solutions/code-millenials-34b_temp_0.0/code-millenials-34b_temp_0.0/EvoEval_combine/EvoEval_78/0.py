
def solve_and_count(s):
    vowels = 'AEIOU'
    new_s = ''
    vowel_count = 0
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].islower():
                new_s += s[i].upper()
            else:
                new_s += s[i].lower()
        else:
            new_s += s[i]
    if not new_s.isalpha():
        new_s = new_s[::-1]
    for i in range(0, len(new_s), 2):
        if new_s[i] in vowels:
            vowel_count += 1
    return (new_s, vowel_count)