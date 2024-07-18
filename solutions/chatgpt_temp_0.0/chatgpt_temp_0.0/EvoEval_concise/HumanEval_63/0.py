

def fibfib(n: int):
    """This function calculates the n-th element of the FibFib sequence.
    The FibFib sequence is defined as:
    fibfib(0) = 0,
    fibfib(1) = 0,
    fibfib(2) = 1,
    fibfib(n) = fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    It returns the n-th element of this sequence.
    
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fibfib_n_minus_1 = 1
        fibfib_n_minus_2 = 0
        fibfib_n_minus_3 = 0
        fibfib_n = 0
        for i in range(3, n + 1):
            fibfib_n = fibfib_n_minus_1 + fibfib_n_minus_2 + fibfib_n_minus_3
            fibfib_n_minus_3 = fibfib_n_minus_2
            fibfib_n_minus_2 = fibfib_n_minus_1
            fibfib_n_minus_1 = fibfib_n
        return fibfib_n