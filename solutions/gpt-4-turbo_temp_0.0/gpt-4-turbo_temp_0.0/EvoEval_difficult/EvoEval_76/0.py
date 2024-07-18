def complex_power(x, n, m):
    if n == 1 or m == 1:
        return False
    p = 2
    while n ** p <= x and m ** p <= x:
        if n ** p * m ** p == x:
            return True
        p += 1
    return False