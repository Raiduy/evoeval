

def fizz_buzz(n: int) -> int:
    """
    Given an integer 'n', this function calculates and returns the number of times the digit '7' occurs in all integers 
    less than 'n' which are divisible either by 11 or 13. The argument to the function, 'n', is an integer and the 
    function returns an integer which represents the count of occurrences of digit '7'.
    
    The function does not consider the number 'n' itself, only the numbers less than 'n'. If an integer less than 'n' 
    is divisible by both 11 and 13, it is only counted once. Here, divisibility is defined in the standard way, i.e., 
    a number 'x' is divisible by a number 'y' if the remainder when 'x' is divided by 'y' is zero.

    The function has no side effects. It does not modify the input argument or any global state. It is purely a 
    computation based on the input argument.

    Examples:

    If the input to the function is 50, '7' appears zero times. Hence the function returns 0.

    >>> fizz_buzz(50)
    0

    If the input to the function is 78, '7' appears 2 times. Hence the function returns 2.

    >>> fizz_buzz(78)
    2

    If the input to the function is 79,' 7' appears 3 times. Hence the function returns 3.

    >>> fizz_buzz(79)
    3
    """
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            count += str(i).count('7')
    return count