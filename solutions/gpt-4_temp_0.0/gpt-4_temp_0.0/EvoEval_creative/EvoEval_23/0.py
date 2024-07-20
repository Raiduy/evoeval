def prime_cipher(s: str):

    def generate_primes(n):
        primes = []
        candidate = 2
        while len(primes) < n:
            if all((candidate % prime != 0 for prime in primes)):
                primes.append(candidate)
            candidate += 1
        return primes
    primes = generate_primes(26)
    prime_dict = {chr(97 + i): str(primes[i]) for i in range(26)}
    return ''.join((prime_dict.get(c, c) for c in s))