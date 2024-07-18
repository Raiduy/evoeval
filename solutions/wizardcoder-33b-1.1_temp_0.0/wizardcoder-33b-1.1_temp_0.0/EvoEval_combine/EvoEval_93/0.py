
def prime_vowel(string):
    vowels = 'aeiouAEIOU'
    for i in range(len(string) - 2, 0, -1):
        if string[i] in vowels and string[i - 1] not in vowels and (string[i + 1] not in vowels):
            return string[i]
    return '' if is_prime(len(string)) else ''