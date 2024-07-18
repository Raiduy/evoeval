
def get_closest_upper_vowel(word):
    vowels = 'AEIOU'
    for i in range(len(word) - 2, 0, -1):
        if word[i] in vowels and word[i - 1].isalpha() and word[i + 1].isalpha() and word[i - 1].islower() and word[i + 1].islower():
            return word[i]
    return ''