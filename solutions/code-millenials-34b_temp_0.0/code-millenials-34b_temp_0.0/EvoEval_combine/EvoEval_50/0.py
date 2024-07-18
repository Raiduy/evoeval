
def get_closest_upper_vowel(word):
    vowels = 'AEIOU'
    word = word[::-1]
    for i in range(1, len(word) - 1, 2):
        if word[i] in vowels and word[i - 1] not in vowels and (word[i + 1] not in vowels):
            return word[i]
    return ''