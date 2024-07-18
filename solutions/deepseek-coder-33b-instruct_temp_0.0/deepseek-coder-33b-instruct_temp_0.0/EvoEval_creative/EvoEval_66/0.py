def prime_anagram_pairs(n):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_anagram(num1, num2):
        return sorted(str(num1)) == sorted(str(num2))
    primes = [num for num in range(2, n + 1) if is_prime(num)]
    pairs = []
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            if is_anagram(primes[i], primes[j]):
                pairs.append((primes[i], primes[j]))
    return pairs