def largest_prime_factor_or_value(n, x, y):
    if n == 1:
        return y
    elif is_prime(n):
        return x
    else:
        return largest_prime_factor(n)