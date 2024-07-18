def special_factorial(n):
    """Computes the Brazilian factorial, a variant of factorial, calculated as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    n should be a positive integer.

    Example:
    >>> special_factorial(4)
    288
    """

    def factorial(x):
        """Helper function to compute factorial of a number."""
        if x == 0 or x == 1:
            return 1
        else:
            return x * factorial(x - 1)
    result = 1
    for i in range(1, n + 1):
        result *= factorial(i)
    return result