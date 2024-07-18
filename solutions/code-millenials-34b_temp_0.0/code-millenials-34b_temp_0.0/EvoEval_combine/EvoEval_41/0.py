
def shifted_upper_count(s, shift):
    upper_vowels = 'AEIOU'
    shift %= len(s)
    if shift > 0:
        s = s[-shift:] + s[:-shift]
    else:
        s = s[shift:] + s[:shift]
    count = 0
    for i in range(0, len(s), 2):
        if s[i] in upper_vowels:
            count += 1
    return count