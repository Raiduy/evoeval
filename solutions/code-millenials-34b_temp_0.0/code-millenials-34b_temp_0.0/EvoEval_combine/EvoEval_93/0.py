
def prime_vowel(string):
    if not is_prime(len(string)):
        return ''
    vowels = 'AEIOUaeiou'
    string = string[::-1]
    for i in range(1, len(string) - 1):
        if string[i] in vowels and string[i - 1] not in vowels and (string[i + 1] not in vowels):
            return string[i]
    return ''