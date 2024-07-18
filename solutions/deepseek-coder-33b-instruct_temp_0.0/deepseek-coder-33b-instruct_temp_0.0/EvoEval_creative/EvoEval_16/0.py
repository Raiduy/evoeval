def fibonacci_sum(n):
    """
    Given a positive integer n, return the sum of the first n numbers in the Fibonacci sequence.
    The Fibonacci sequence is a series of numbers where a number is the sum of the two preceding ones, starting with 0 and 1.
    
    >>> fibonacci_sum(1)
    0
    >>> fibonacci_sum(2)
    1
    >>> fibonacci_sum(3)
    2
    >>> fibonacci_sum(10)
    88
    >>> fibonacci_sum(20)
    10945
    >>> fibonacci_sum(30)
    1346268
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
        return sum(fib_sequence)