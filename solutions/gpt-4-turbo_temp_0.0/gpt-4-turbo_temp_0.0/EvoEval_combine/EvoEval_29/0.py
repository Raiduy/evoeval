def largest_prime_factor_or_value(n, x, y):
    """A program which should return the largest prime factor of n if n is not a prime number, should return the value of x if n is a prime number and y if n is 1."""
    if n == 1:
        return y
    elif is_prime(n):
        return x
    else:
        return largest_prime_factor(n)