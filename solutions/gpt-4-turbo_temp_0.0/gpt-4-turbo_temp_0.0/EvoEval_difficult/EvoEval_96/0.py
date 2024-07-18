def prime_sequences(n, m):
    """Implement a function that takes two non-negative integers n and m. The function should return a 2D array of the first n sub-sequences, each of length m, of prime numbers less than n.
    The function should return an empty list if n or m is 0.
    """
    if n == 0 or m == 0:
        return []
    primes = [i for i in range(2, n) if is_prime(i)]
    sequences = []
    for i in range(len(primes)):
        if i + m <= len(primes):
            sequences.append(primes[i:i + m])
        else:
            break
    return sequences[:n]