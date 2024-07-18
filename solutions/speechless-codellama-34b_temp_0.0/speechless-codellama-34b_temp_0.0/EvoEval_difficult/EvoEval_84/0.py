def enhanced_solve(N, M):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def sum_of_digits(n):
        return sum((int(digit) for digit in bin(n)[2:]))
    primes = [i for i in range(N, M + 1) if is_prime(i)]
    total_sum = sum_of_digits(N) + sum_of_digits(M)
    result = total_sum * len(primes)
    return bin(result)[2:]