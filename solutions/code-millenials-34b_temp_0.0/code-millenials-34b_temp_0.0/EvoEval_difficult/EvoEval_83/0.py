def starts_one_ends(n, x, y):
    if not 1 <= n <= 5 or not 0 <= x <= 9 or (not 0 <= y <= 9):
        return -1
    count = 0
    for i in range(10 ** (n - 1), 10 ** n):
        str_i = str(i)
        if str_i[0] == str(x) or str_i[-1] == str(y):
            count += 1
    return count