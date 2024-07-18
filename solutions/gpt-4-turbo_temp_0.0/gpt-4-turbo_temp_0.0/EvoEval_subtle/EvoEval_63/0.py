
def fibfib(n: int, memo={}):
    """The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-3) + fibfib(n-2) - fibfib(n-1).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    -2
    >>> fibfib(8)
    4
    """
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        memo[n] = fibfib(n - 3, memo) + fibfib(n - 2, memo) - fibfib(n - 1, memo)
        return memo[n]