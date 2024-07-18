

def sum_to_n(n: int) -> int:
    """
    The function sum_to_n is a mathematical function that calculates the cumulative sum of all integer numbers starting 
    from 1 to the input integer number n inclusive. This calculation can also be understood as finding the sum of an 
    arithmetic series.

    The function takes one argument:
    - n (int): An integer number which is the end point for the series sum. This number is included in the series. 
               It is expected to be a positive integer, as the function does not handle negative numbers or zero.

    The function returns an integer that is the sum of all integers from 1 to n.

    Here are some example uses of the function:

    >>> sum_to_n(30)
    465
    This means that the sum of all integers from 1 to 30 is 465.

    >>> sum_to_n(100)
    5050
    This means that the sum of all integers from 1 to 100 is 5050.

    >>> sum_to_n(5)
    15
    This means that the sum of all integers from 1 to 5 is 15.

    >>> sum_to_n(10)
    55
    This means that the sum of all integers from 1 to 10 is 55.

    >>> sum_to_n(1)
    1
    This means that the sum of all integers from 1 to 1 is 1, i.e., just the number itself.
    """
    return n * (n + 1) // 2