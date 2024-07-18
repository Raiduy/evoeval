def prime_cipher(s: str):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
    mapping = {chr(i + 96): str(primes[i - 1]) for i in range(1, 27)}
    return ''.join((mapping.get(c, c) for c in s))