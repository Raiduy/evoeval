
def x_or_y(n, x, y):
    """Returns x if n is prime, otherwise returns y.

    Examples:
    x_or_y(7, 34, 12) returns 34
    x_or_y(15, 8, 5) returns 5
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
    if is_prime(n):
        return x
    else:
        return y