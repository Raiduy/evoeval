
def odd_fibfib(n: int):
    """The Odd FibFib sequence is a sequence similar to the FibFib sequence that's defined as follows:
    odd_fibfib(0) == 0
    odd_fibfib(1) == 0
    odd_fibfib(2) == 1
    odd_fibfib(n) == odd_fibfib(n-1) + odd_fibfib(n-2) + odd_fibfib(n-3).
    However, if the result is an even number, it is replaced by the product of its odd digits. If all digits are even, it is replaced by 0.
    Please write a function to compute the n-th element of the odd_fibfib sequence efficiently.
    >>> odd_fibfib(1)
    0
    >>> odd_fibfib(5)
    0
    >>> odd_fibfib(7)
    1
    >>> odd_fibfib(9)
    0
    """
    if n < 3:
        return [0, 0, 1][n]
    else:
        fibfib = [0, 0, 1] + [0] * (n - 2)
        for i in range(3, n + 1):
            fibfib[i] = fibfib[i - 1] + fibfib[i - 2] + fibfib[i - 3]
            if fibfib[i] % 2 == 0:
                fibfib[i] = product_of_odd_digits(fibfib[i])
        return fibfib[n]