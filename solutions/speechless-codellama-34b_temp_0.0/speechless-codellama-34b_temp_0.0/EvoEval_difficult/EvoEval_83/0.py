def starts_one_ends(n, x, y):
    if n > 5 or n < 1 or (not str(x).isdigit()) or (not str(y).isdigit()):
        return -1
    count = 0
    for i in range(10 ** (n - 1), 10 ** n):
        if str(i)[0] == str(x) or str(i)[-1] == str(y):
            count += 1
    return count