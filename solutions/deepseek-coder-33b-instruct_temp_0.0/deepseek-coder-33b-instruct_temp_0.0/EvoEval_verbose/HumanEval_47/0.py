

def median(l: list):
    """
    This function calculates and returns the median value of a given list of numbers named 'l'. If the list 'l' has an 
    odd number of elements, the median is the middle number. If the list 'l' has an even number of elements, the median 
    is calculated as the average of the two middle numbers. 

    The median is a measure of central tendency that can give a better sense of the typical value of a set of numbers 
    in the list 'l' compared to the average, especially in skewed distributions.

    Args:
    l (list of int/float): A list of numbers. This list must be non-empty and can contain any number of elements. 
    The numbers can be any real numbers (integers or floating point).

    Returns:
    int/float: The function will return the median value as an integer if the list 'l' has an odd number of elements. 
    If the list 'l' has an even number of elements, the median value will be returned as a float.

    Examples:
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    n = len(l)
    s = sorted(l)
    return (sum(s[n // 2 - 1:n // 2 + 1]) / 2.0, s[n // 2])[n % 2]