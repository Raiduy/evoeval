def complex_power(x, n, m):
    if n == 1 or m == 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            power_n = 0
            power_m = 0
            while x % i == 0:
                x //= i
                power_n += 1
            while x % i == 0:
                x //= i
                power_m += 1
            if x == 1 and power_n % n == 0 and (power_m % m == 0):
                return True
    if x > 1 and n == 1 and (m == 1):
        return True
    return False