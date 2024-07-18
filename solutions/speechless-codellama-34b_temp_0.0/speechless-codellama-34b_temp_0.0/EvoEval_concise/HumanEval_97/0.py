def multiply(a, b):
    """
    Returns the product of the unit digits of two integers.
    Examples:
    multiply(148, 412) -> 16
    multiply(19, 28) -> 72
    multiply(2020, 1851) -> 0
    multiply(14,-15) -> 20
    """
    unit_digit_a = abs(a) % 10
    unit_digit_b = abs(b) % 10
    return unit_digit_a * unit_digit_b