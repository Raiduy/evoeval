

def truncate_number(number: float) -> float:
    """
    Decomposes a positive float into its integer and decimal parts,
    then returns the decimal part.
    
    >>> truncate_number(3.5)
    0.5
    """
    if number < 0:
        raise ValueError('The number must be positive.')
    integer_part = int(number)
    decimal_part = number - integer_part
    return decimal_part