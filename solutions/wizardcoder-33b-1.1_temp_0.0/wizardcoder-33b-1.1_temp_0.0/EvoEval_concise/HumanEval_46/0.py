

def fib4(n: int):
    if n in {0, 1, 3}:
        return 0 if n == 0 else 1 if n == 1 else 2
    elif n == 2:
        return 2
    else:
        (a, b, c, d) = (0, 1, 2, 2)
        for _ in range(n - 3):
            (a, b, c, d) = (b, c, d, a + b + c + d)
        return d