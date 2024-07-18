

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # Extract the integer part of the number
    integer_part = int(number)
    # Subtract the integer part from the original number to get the decimal part
    decimal_part = number - integer_part
    return decimal_part
