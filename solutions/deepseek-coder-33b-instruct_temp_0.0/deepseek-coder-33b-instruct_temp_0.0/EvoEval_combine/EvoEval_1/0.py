def round_and_flip(value: str) -> str:
    """
    Create a function that takes a value representing two parts (number and string)
    and returns a string with two parts: 1) The closest integer to the number,
    and 2) The string with its case flipped. If the number is equidistant from two integers,
    round it away from zero. Between these two parts, add a space. 

    Examples
    >>> round_and_flip("10.5abc")
    '11 ABC'
    >>> round_and_flip("15.3ABC")
    '15 abc'

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example round_and_flip("14.5abc") should
    return '15 ABC' and round_and_flip("-14.5ABC") should return '-15 abc'.
    """
    (num_part, str_part) = (value.split('.')[0], value.split('.')[1])
    num_part = round(float(num_part))
    str_part = str_part.swapcase()
    return f'{num_part} {str_part}'