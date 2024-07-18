def largest_prime_factor_or_value(n, x, y):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def largest_prime_factor(n):
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
        return n
    if n == 1:
        return y
    elif is_prime(n):
        return x
    else:
        return largest_prime_factor(n)