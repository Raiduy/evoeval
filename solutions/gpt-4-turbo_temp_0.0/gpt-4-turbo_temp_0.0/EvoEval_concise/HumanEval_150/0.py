
def x_or_y(n, x, y):
    """Returns x if n is prime, otherwise returns y.

    Examples:
    x_or_y(7, 34, 12) returns 34
    x_or_y(15, 8, 5) returns 5
    """
    return x if is_prime(n) else y