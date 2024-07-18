
def starts_one_ends(n):
    if n == 1:
        return 2
    elif n == 2:
        return 4
    else:
        return 2 * 10 ** (n - 1)