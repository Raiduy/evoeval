def largest_divisor(n: int) -> int:
    """
    This function, named 'largest_divisor', is designed to find the largest integer that divides a given input integer 'n' without leaving any remainder. 
    The integer returned is always smaller than the input integer 'n' since it doesn't consider 'n' itself as a possible divisor. 
    
    Parameters:
    n (int): The input integer for which we want to find the largest divisor.
    
    Returns:
    int: The largest integer smaller than 'n' that can evenly divide 'n'.
    
    Example:
    >>> largest_divisor(15)
    5
    The example given uses 15 as the input integer 'n'. The function finds that the largest integer smaller than 'n' that can evenly divide 'n' is 5.
    This is because 5 is the largest number that can divide 15 without leaving any remainder.
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
    return None