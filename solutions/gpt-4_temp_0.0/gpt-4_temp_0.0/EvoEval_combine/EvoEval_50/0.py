
def get_closest_upper_vowel(word):
    vowels = 'AEIOU'
    consonants = 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'
    for i in range(len(word) - 1, -1, -2):
        if word[i] in vowels and i != 0 and (i != len(word) - 1):
            if word[i - 1] in consonants and word[i + 1] in consonants:
                return word[i]
    return ''