
def x_or_y(n, x, y):
    """Returns x if n is prime, otherwise returns y.

    Examples:
    x_or_y(7, 34, 12) returns 34
    x_or_y(15, 8, 5) returns 5
    """

    def is_prime(n):
        """Checks if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    if is_prime(n):
        return x
    else:
        return y