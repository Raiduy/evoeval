def prime_cipher(s: str) -> str:

    def generate_primes(n):
        primes = []
        num = 2
        while len(primes) < n:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)
            num += 1
        return primes
    letters_to_primes = {chr(97 + i): prime for (i, prime) in enumerate(generate_primes(26))}
    result = ''
    for char in s:
        if char.islower():
            result += str(letters_to_primes[char])
        else:
            result += char
    return result