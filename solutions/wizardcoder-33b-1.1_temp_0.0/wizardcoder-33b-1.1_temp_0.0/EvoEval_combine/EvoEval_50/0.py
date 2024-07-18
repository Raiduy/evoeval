
def get_closest_upper_vowel(word):
    vowels = 'AEIOU'
    for i in range(len(word) - 2, 0, -1):
        if word[i] in vowels and i % 2 == 0:
            return word[i]
    return ''