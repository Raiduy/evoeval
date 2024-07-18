
def fib4(n: int) -> str:
    fib = [0, 0, 2, 0]
    if n < 4:
        return str(fib[n])
    for i in range(4, n + 1):
        fib.append(fib[i - 1] + fib[i - 2] + fib[i - 3] + fib[i - 4])
    return str(fib[n])