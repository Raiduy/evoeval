def count_spec_chars(s, m, n):
    if len(s) < m or len(s) > n:
        return -1
    vowels = ['A', 'E', 'I', 'O', 'U']
    consonants = [chr(i) for i in range(ord('a'), ord('z') + 1) if chr(i) not in vowels]
    sum_uppercase_vowels = 0
    sum_lowercase_consonants = 0
    for i in range(len(s)):
        if i % 2 == 0 and s[i].isupper() and (s[i] in vowels):
            sum_uppercase_vowels += ord(s[i])
        elif i % 2 != 0 and s[i].islower() and (s[i] in consonants):
            sum_lowercase_consonants += ord(s[i])
    return (sum_uppercase_vowels, sum_lowercase_consonants)