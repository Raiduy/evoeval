def fib(n: int, x: int, operation: str) -> int:
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        fib_numbers = [0, 1, 1]
        for i in range(3, n + 1):
            if i % x == 0:
                if operation == 'square':
                    fib_numbers.append(fib_numbers[i - 1] ** 2)
                elif operation == 'add_two':
                    fib_numbers.append(fib_numbers[i - 1] + 2)
                else:
                    fib_numbers.append(0)
            else:
                fib_numbers.append(fib_numbers[i - 1] + fib_numbers[i - 2])
        return fib_numbers[n]