
def fibfib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        (a, b, c) = (0, 0, 1)
        for _ in range(n - 3):
            (a, b, c) = (b, c, a + b - c)
        return c