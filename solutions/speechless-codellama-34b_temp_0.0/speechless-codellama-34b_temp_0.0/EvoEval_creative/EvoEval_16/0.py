def fibonacci_sum(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        (a, b) = (0, 1)
        total = 0
        for i in range(n):
            total += a
            (a, b) = (b, a + b)
        return total