
def shifted_upper_count(s, shift):
    vowels = 'AEIOU'
    count = 0
    if shift > len(s):
        s = s[::-1]
    for i in range(len(s)):
        if i % 2 == 0 and s[i].isupper() and (s[i] in vowels):
            count += 1
    return count