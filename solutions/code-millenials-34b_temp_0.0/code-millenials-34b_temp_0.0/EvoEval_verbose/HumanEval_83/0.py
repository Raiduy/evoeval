
def starts_one_ends(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    else:
        return 2 * 10 ** (n - 1)