def modp(n: int, p: int, m: int):
    if m % p == 0:
        return -1
    return (pow(2, n, p) + m) % p