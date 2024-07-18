def fib(n: int, x: int, operation: str) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        (a, b) = (0, 1)
        for i in range(2, n + 1):
            if i % x == 0:
                if operation == 'square':
                    b = b ** 2
                elif operation == 'add_two':
                    b += 2
                elif operation == 'skip':
                    b = 0
            (a, b) = (b, a + b)
        return b