def prime_anagram_pairs(n):
    primes = [i for i in range(2, n) if is_prime(i)]
    pairs = []
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            if are_anagrams(primes[i], primes[j]):
                pairs.append((primes[i], primes[j]))
    return pairs