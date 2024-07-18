def special_factorial(n):
    """Computes the Brazilian factorial, a variant of factorial, calculated as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    n should be a positive integer.

    Example:
    >>> special_factorial(4)
    288
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError('n should be a positive integer.')

    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)
    result = 1
    for i in range(1, n + 1):
        result *= factorial(i)
    return result