def enhanced_solve(N, M):
    """Given two positive integers N and M, compute the total sum of their digits in binary,
    then multiply by the number of primes between N and M, inclusive.
    Final result should be a binary string."""
    total_binary_sum = sum_of_binary_digits(N) + sum_of_binary_digits(M)
    prime_count = count_primes(N, M)
    result = total_binary_sum * prime_count
    return bin(result)[2:]