
def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the sum of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 10.
    multiply(19, 28) should return 17.
    multiply(2020, 1851) should return 1.
    multiply(14,-15) should return 9.
    """
    unit_digit_a = abs(a) % 10
    unit_digit_b = abs(b) % 10
    return unit_digit_a + unit_digit_b