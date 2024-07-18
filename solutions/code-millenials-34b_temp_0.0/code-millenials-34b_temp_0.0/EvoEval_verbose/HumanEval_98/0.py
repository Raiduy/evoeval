
def count_upper(s):
    upper_vowels = 'AEIOU'
    count = 0
    for i in range(0, len(s), 2):
        if s[i] in upper_vowels:
            count += 1
    return count