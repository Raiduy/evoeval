def fibonacci_sum(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    fib_n_minus_2 = 0
    fib_n_minus_1 = 1
    sum_fib = 1
    for _ in range(2, n):
        fib_n = fib_n_minus_1 + fib_n_minus_2
        sum_fib += fib_n
        fib_n_minus_2 = fib_n_minus_1
        fib_n_minus_1 = fib_n
    return sum_fib