def largest_prime_factor_or_value(n, x, y):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    if n == 1:
        return y
    elif is_prime(n):
        return x
    else:
        for i in range(2, n):
            if n % i == 0 and is_prime(n // i):
                return n // i
        return x