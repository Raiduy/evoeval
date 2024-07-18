
def get_closest_upper_vowel(word):
    vowels = 'AEIOU'
    reversed_word = word[::-1]
    for i in range(1, len(reversed_word) - 1):
        if reversed_word[i] in vowels and (len(word) - 1 - i) % 2 == 0:
            if reversed_word[i - 1].isalpha() and reversed_word[i + 1].isalpha() and (reversed_word[i - 1].upper() not in vowels) and (reversed_word[i + 1].upper() not in vowels):
                return reversed_word[i]
    return ''