
def modp(n: int, p: int, q: int) -> int:
    return pow(2, n + q, p)