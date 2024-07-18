
def get_closest_upper_vowel(word):
    vowels = 'AEIOU'
    for i in range(len(word) - 1, 0, -2):
        if word[i] in vowels and word[i - 1].islower() and word[i + 1].islower():
            return word[i]
    return ''