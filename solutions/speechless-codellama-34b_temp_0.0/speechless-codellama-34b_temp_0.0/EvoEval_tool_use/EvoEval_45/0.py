def valid_input(string):
    """Check if a string only contains digits and returns True if valid, False otherwise.
    Args:
        string: a string
    Returns:
        True if the string only contains digits, False otherwise.
    """
    return string.isdigit()
def from_string_to_list(digit_string):
    """Given a string of digits, return a list of integers.
    If the string contains non-digit characters, return an empty list.
    """
    if valid_input(digit_string):
        return [int(digit) for digit in digit_string]
    else:
        return []