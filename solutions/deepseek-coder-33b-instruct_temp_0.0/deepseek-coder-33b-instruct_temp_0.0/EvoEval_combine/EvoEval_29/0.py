def largest_prime_factor_or_value(n, x, y):
    """A program which should return the largest prime factor of n if n is not a prime number, should return the value of x if n is a prime number and y if n is 1. 

    Examples:
    for largest_prime_factor_or_value(13195, 34, 12) == 29
    for largest_prime_factor_or_value(7, 8, 5) == 8
    for largest_prime_factor_or_value(1, 8, 5) == 5
    """

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def largest_prime_factor(n):
        max_prime = -1
        while n % 2 == 0:
            max_prime = 2
            n >>= 1
        while n % 3 == 0:
            max_prime = 3
            n = n / 3
        for i in range(5, int(n ** 0.5) + 1, 6):
            while n % i == 0:
                max_prime = i
                n = n / i
            while n % (i + 2) == 0:
                max_prime = i + 2
                n = n / (i + 2)
        if n > 4:
            max_prime = n
        return int(max_prime)
    if n == 1:
        return y
    elif is_prime(n):
        return x
    else:
        return largest_prime_factor(n)