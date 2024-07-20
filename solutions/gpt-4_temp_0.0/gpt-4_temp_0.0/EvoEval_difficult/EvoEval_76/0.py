def complex_power(x, n, m):
    if n == 1 or m == 1:
        return False
    for i in range(1, 101):
        if n ** i == m ** i == x:
            return True
    return False