def magical_multiply(s1, s2):
    """
    In the mystical land of Pyth, numbers behave quite differently. Here, when two numbers are multiplied, the result is given by the sum of all possible unique combinations of their digits. 

    For example, if two numbers 24 and 13 are multiplied, the result would be the sum of all unique combinations of digits (2, 4) and (1, 3). The combinations would be (2, 1), (2, 3), (4, 1) and (4, 3) and their sums would be 3, 5, 5 and 7, and hence the result of the multiplication would be 3 + 5 + 5 + 7 = 20.

    The function magical_multiply(s) would take in two positive integers as input (in string format) and should return their product according to the laws of the land of Pyth.

    For example:
    >>> magical_multiply('24', '13')
    20
    >>> magical_multiply('56', '79')
    54
    """
    digits1 = list(map(int, s1))
    digits2 = list(map(int, s2))
    sum_of_combinations = 0
    for digit1 in digits1:
        for digit2 in digits2:
            sum_of_combinations += digit1 + digit2
    return sum_of_combinations