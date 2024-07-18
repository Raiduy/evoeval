def count_spec_chars(s, m, n):
    if len(s) < m or len(s) > n:
        return -1
    vowels = 'AEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    ascii_sum_vowels = 0
    ascii_sum_consonants = 0
    for i in range(len(s)):
        if s[i].isalpha():
            if i % 2 == 0:
                if s[i] in vowels:
                    ascii_sum_vowels += ord(s[i])
            elif s[i] in consonants:
                ascii_sum_consonants += ord(s[i])
    return (ascii_sum_vowels, ascii_sum_consonants)