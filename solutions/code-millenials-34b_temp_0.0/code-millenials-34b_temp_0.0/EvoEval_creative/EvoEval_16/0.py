def fibonacci_sum(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        (a, b) = (0, 1)
        total_sum = 1
        for _ in range(2, n):
            (a, b) = (b, a + b)
            total_sum += b
        return total_sum