
def prime_vowel(string):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    vowels = 'aeiouAEIOU'
    if is_prime(len(string)):
        for i in range(len(string) - 1, 0, -1):
            if string[i] in vowels and string[i - 1] not in vowels and (string[i + 1] not in vowels):
                return string[i]
    return ''