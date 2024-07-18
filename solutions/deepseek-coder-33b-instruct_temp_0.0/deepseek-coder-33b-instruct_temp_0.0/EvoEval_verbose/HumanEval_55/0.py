

def fib(n: int):
    """
    This function calculates and returns the n-th number in the Fibonacci sequence.

    The Fibonacci sequence is a series of numbers in which each number is the sum 
    of the two preceding ones, usually starting with 0 and 1. In this case, 
    the function fib starts counting from 1, meaning fib(1) will return the first 
    number in the sequence (1), fib(2) will return the second number (1 as well), 
    fib(3) will return the third number (2), and so forth.

    This function uses a recursive algorithm to calculate the Fibonacci number 
    and requires an integer input (n) that specifies the position in the Fibonacci sequence.

    Args:
        n (int): The position in the Fibonacci sequence for which to return the number. 
                 This should be a positive integer.

    Returns:
        int: The n-th number in the Fibonacci sequence.

    Examples:
        >>> fib(10)
        55
        >>> fib(1)
        1
        >>> fib(8)
        21
    """
    if n <= 0:
        print('Input should be a positive integer.')
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)