
def even_odd_count(num):
    """
    Given an integer as an input 'num', this function aims to return a tuple. The tuple contains two elements, the first element represents the count of even digits in 'num' and the second element represents the count of odd digits in 'num'. 

    The function operates by examining each digit in the absolute value of the input integer 'num', categorizing each digit as either even or odd, then counting the total number of each. Negative integers are treated the same as their positive counterparts, as the function processes the absolute value of 'num'. Hence, the sign of 'num' does not affect the output. 

    The function returns a tuple in the format (even_count, odd_count), where 'even_count' is the number of even digits and 'odd_count' is the number of odd digits in 'num'.

    Parameters:
    num (int): an integer whose digits are to be categorized and counted as either even or odd.

    Returns:
    tuple: A tuple in the format (even_count, odd_count), where 'even_count' is the number of even digits and 'odd_count' is the number of odd digits in 'num'.

    Examples:
    >>> even_odd_count(-12)
    (1, 1)

    This example returns (1, 1) because the number -12 contains one even digit (2) and one odd digit (1).
    
    >>> even_odd_count(123)
    (1, 2)

    This example returns (1, 2) because the number 123 contains one even digit (2) and two odd digits (1, 3).
    """
    num = abs(num)
    even_count = 0
    odd_count = 0
    while num > 0:
        digit = num % 10
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        num = num // 10
    return (even_count, odd_count)