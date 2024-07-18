
def starts_one_ends(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError('Input must be a positive integer')
    if n == 1:
        return 2
    else:
        return 10 * 10 ** (n - 2) + 10