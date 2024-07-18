def count_spec_chars(s, m, n):
    if len(s) < m or len(s) > n:
        return -1
    upper_vowels = 'AEIOU'
    lower_consonants = 'bcdfghjklmnpqrstvwxyz'
    ascii_upper_sum = 0
    ascii_lower_sum = 0
    for i in range(len(s)):
        if i % 2 == 0 and s[i] in upper_vowels:
            ascii_upper_sum += ord(s[i])
        elif i % 2 == 1 and s[i] in lower_consonants:
            ascii_lower_sum += ord(s[i])
    return (ascii_upper_sum, ascii_lower_sum)