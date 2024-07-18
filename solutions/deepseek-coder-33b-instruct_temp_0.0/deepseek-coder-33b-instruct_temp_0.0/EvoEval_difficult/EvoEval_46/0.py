def fib4_memo(n: int, m: int):
    if n < 0 or m > n:
        return 'Invalid input'
    fib4_sequence = [0, 0, 2, 0]
    for i in range(4, n + 1):
        fib4_sequence.append(fib4_sequence[i - 1] + fib4_sequence[i - 2] + fib4_sequence[i - 3] + fib4_sequence[i - 4])
    return fib4_sequence[-m]