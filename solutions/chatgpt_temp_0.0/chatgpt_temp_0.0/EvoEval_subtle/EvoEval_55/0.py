
def fib(n: int):
    """Return (n+1)-th Fibonacci number.
    >>> fib(10)
    89
    >>> fib(1)
    1
    >>> fib(8)
    34
    """
    if n <= 1:
        return n
    else:
        fib_list = [0, 1]
        for i in range(2, n + 1):
            fib_list.append(fib_list[i - 1] + fib_list[i - 2])
        return fib_list[n]