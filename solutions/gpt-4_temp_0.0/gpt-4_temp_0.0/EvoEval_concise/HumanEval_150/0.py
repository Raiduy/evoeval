
def x_or_y(n, x, y):
    """Returns x if n is prime, otherwise returns y.

    Examples:
    x_or_y(7, 34, 12) returns 34
    x_or_y(15, 8, 5) returns 5
    """

    def is_prime(num):
        """Check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    return x if is_prime(n) else y