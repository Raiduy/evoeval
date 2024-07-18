def enhanced_solve(N, M):
    """Given two positive integers N and M, compute the total sum of their digits in binary,
    then multiply by the number of primes between N and M, inclusive.
    Final result should be a binary string
    """
    sum_of_digits = sum((int(digit) for digit in bin(N)[2:] + bin(M)[2:]))
    num_of_primes = sum((is_prime(i) for i in range(N, M + 1)))
    result = sum_of_digits * num_of_primes
    return bin(result)[2:]