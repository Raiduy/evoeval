

def fib4(n: int) -> int:
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 2
    if n == 3:
        return 0
    fib = [0, 0, 2, 0]
    for i in range(4, n+1):
        fib.append(fib[i-1] + fib[i-2] + fib[i-3] + fib[i-4])
    return fib[n]
