

def sum_to_n(n: int) -> int:
    """
    The function sum_to_n is a mathematical function that calculates the cumulative sum of all integer numbers starting 
    from 1 to the input integer number n inclusive. This calculation can also be understood as finding the sum of an 
    arithmetic series.

    The function takes one argument:
    - n (int): An integer number which is the end point for the series sum. This number is included in the series. 
               It is expected to be a positive integer, as the function does not handle negative numbers or zero.

    The function returns an integer that is the sum of all integers from 1 to n.
    """
    return sum(range(1, n + 1))