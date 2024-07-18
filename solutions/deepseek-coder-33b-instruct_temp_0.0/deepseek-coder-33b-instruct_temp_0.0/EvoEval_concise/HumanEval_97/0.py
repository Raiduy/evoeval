def multiply(a, b):
    """
    Returns the product of the unit digits of two integers.
    Examples:
    multiply(148, 412) -> 16
    multiply(19, 28) -> 72
    multiply(2020, 1851) -> 0
    multiply(14,-15) -> 20
    """
    a_unit = abs(a) % 10
    b_unit = abs(b) % 10
    return a_unit * b_unit