

def fibfib(n: int):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fibfib_numbers = [0, 0, 1]
        for i in range(3, n + 1):
            fibfib_numbers.append(fibfib_numbers[i - 1] + fibfib_numbers[i - 2] + fibfib_numbers[i - 3])
        return fibfib_numbers[n]
