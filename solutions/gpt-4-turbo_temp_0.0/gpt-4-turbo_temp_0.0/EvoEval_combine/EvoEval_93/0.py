
def prime_vowel(string):
    vowels = 'aeiouAEIOU'
    if not is_prime(len(string)):
        return ''
    for i in range(len(string) - 2, 0, -1):
        if string[i] in vowels and (not string[i + 1] in vowels) and (not string[i - 1] in vowels):
            return string[i]
    return ''