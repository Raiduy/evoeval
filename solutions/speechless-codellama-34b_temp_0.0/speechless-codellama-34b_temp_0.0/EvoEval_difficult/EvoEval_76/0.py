def complex_power(x, n, m):
    if n == 1 or m == 1:
        return False
    else:
        int_n = int(n)
        int_m = int(m)
        if int_n == int_m:
            if n ** int_n == m ** int_m == x:
                return True
            else:
                return False
        else:
            return False