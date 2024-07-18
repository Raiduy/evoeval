
def x_or_y(n, x, y):
    """Returns x if n is prime, otherwise returns y."""
    if is_prime(n):
        return x
    else:
        return y