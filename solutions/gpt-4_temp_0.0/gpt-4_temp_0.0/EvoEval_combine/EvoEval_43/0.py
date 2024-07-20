
def sorted_fib4_sequence(n: int):
    """The sorted Fib4 sequence is a sequence similar to the Fib4 sequence 
    that's defined as follows:

    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    
    However, for the sorted Fib4 sequence we are not just interested in a single element but rather 
    the entire sequence up to the n-th element.
    Furthermore, depending on the sum of the first and last elements of the sequence, 
    you will sort the sequence in ascending order if the sum is odd, 
    or sort it in descending order if the sum is even.
    Please write a function to efficiently compute the sorted Fib4 sequence.  Do not use recursion.

    Examples:
    >>> sorted_fib4_sequence(5)
    [0, 0, 0, 2, 2]
    >>> sorted_fib4_sequence(6)
    [4, 2, 2, 0, 0, 0]
    >>> sorted_fib4_sequence(7)
    [8, 4, 2, 2, 0, 0, 0]
    """
    fib4 = [0, 0, 2, 0]
    for i in range(4, n):
        fib4.append(fib4[i - 1] + fib4[i - 2] + fib4[i - 3] + fib4[i - 4])
    fib4 = fib4[:n]
    if (fib4[0] + fib4[-1]) % 2 == 0:
        fib4.sort(reverse=True)
    else:
        fib4.sort()
    return fib4