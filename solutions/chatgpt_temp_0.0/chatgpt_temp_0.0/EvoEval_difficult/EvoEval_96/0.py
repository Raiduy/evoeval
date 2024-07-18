def prime_sequences(n, m):
    if n == 0 or m == 0:
        return []
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    sequences = []
    for i in range(len(primes) - m + 1):
        sequence = primes[i:i + m]
        sequences.append(sequence)
    return sequences