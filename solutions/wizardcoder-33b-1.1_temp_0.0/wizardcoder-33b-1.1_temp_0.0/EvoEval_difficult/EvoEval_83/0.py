def starts_one_ends(n, x, y):
    if not 1 <= n <= 5 or not 0 <= x <= 9 or (not 0 <= y <= 9):
        return -1
    count = 0
    start = int('1' + '0' * (n - 1))
    end = int('1' + '0' * n)
    for i in range(start, end):
        if int(str(i)[0]) == x or int(str(i)[-1]) == y:
            count += 1
    return count if count > 0 else -1