

def truncate_number(number: float) -> float:
    """ 
    This function is designed to process a positive floating point number and isolate its decimal part. 

    First, a given floating point number is decomposed into two components: 
    1. An integer part, which is the largest integer that is smaller than or equal to the given number.
    2. A decimal part, which is the leftover part of the number after subtracting the integer part. This part is always smaller than 1.

    The function then returns just the decimal part of the number, effectively truncating the integer part.

    Parameters: 
    number (float): The positive floating point number that will be processed by the function. 
    
    Returns: 
    This function returns a float, representing the decimal part of the input number.

    Example:
    >>> truncate_number(3.5)
    0.5
    """
    integer_part = int(number)
    decimal_part = number - integer_part
    return decimal_part