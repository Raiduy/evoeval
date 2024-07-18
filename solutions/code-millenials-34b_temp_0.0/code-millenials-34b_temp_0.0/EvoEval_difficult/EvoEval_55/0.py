def fib(n: int, x: int, operation: str) -> int:
    fib_list = [0, 1]
    for i in range(2, n + 1):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    for i in range(x, n + 1, x):
        if operation == 'square':
            fib_list[i] = fib_list[i] ** 2
        elif operation == 'add_two':
            fib_list[i] = fib_list[i] + 2
        elif operation == 'skip':
            fib_list[i] = 0
    return fib_list[n]