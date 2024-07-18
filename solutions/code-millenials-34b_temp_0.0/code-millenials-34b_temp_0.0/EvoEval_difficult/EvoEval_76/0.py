def complex_power(x, n, m):
    if n == 1 or m == 1:
        return False
    else:
        for i in range(1, int(x ** 0.5) + 1):
            if n ** i == x and m ** i == x:
                return True
        return False