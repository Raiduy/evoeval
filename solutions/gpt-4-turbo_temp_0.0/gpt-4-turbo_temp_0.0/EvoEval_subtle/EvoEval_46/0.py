
def fib4(n: int) -> str:
    """The Fib4 number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence. Do not use recursion. Return string representation.
    """
    if n == 0:
        return '0'
    elif n == 1:
        return '0'
    elif n == 2:
        return '2'
    elif n == 3:
        return '0'
    (a, b, c, d) = (0, 0, 2, 0)
    for _ in range(4, n + 1):
        temp = a + b + c + d
        (a, b, c, d) = (b, c, d, temp)
    return str(d)