
def odd_fibfib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        (a, b, c) = (0, 0, 1)
        for _ in range(3, n + 1):
            (a, b, c) = (b, c, a + b + c)
            if c % 2 == 0:
                c = 0
                for digit in str(c):
                    if int(digit) % 2 != 0:
                        c *= int(digit)
        return c