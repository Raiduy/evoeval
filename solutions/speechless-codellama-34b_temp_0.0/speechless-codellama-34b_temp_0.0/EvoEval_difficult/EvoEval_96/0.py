def prime_sequences(n, m):
    if n == 0 or m == 0:
        return []
    primes = [i for i in range(n) if is_prime(i)]
    sequences = []
    for i in range(len(primes) - m + 1):
        sequences.append(primes[i:i + m])
    return sequences