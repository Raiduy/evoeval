def modp(n: int, p: int, m: int):
    if m % p == 0:
        return -1
    else:
        return (2 ** n % p + m) % p