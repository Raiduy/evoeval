
def modp(n: int, p: int, q: int) -> int:
    """Return 2^(n+q) modulo p (be aware of numerics)."""
    return pow(2, n + q, p)