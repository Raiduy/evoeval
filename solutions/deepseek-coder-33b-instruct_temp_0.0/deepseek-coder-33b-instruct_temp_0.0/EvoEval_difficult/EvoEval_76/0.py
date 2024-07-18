def complex_power(x, n, m):
    if n == 1 or m == 1:
        return False
    else:
        int_n = int(n ** (1 / 2))
        int_m = int(m ** (1 / 2))
        if int_n ** int_m == x or int_m ** int_n == x:
            return True
        else:
            return False