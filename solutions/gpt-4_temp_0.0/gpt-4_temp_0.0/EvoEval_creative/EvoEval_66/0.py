def prime_anagram_pairs(n):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    primes = [i for i in range(2, n) if is_prime(i)]
    anagram_pairs = []
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            if sorted(str(primes[i])) == sorted(str(primes[j])):
                anagram_pairs.append((primes[i], primes[j]))
    return sorted(anagram_pairs)