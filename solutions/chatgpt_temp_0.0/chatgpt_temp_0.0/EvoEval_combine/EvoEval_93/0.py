
def prime_vowel(string):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = [c for c in string if c.isalpha() and c.lower() not in vowels]
    if is_prime(len(consonants)):
        for i in range(len(string) - 2, 0, -1):
            if string[i] in vowels and string[i - 1] not in vowels and (string[i + 1] not in vowels):
                return string[i]
    return ''