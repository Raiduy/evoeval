def starts_one_ends(n, x, y):
    if not 1 <= n <= 5 or not 0 <= x <= 9 or (not 0 <= y <= 9):
        return -1
    count = 0
    for i in range(10 ** (n - 1), 10 ** n):
        num_str = str(i)
        if num_str[0] == str(x) or num_str[-1] == str(y):
            count += 1
    return count