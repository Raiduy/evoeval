def prime_cipher(s: str):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    result = ''
    for char in s:
        if char.islower() and char.isalpha():
            result += str(primes[ord(char) - ord('a') + 1])
        else:
            result += char
    return result