
def is_nested(string):
    """
    This function checks if the given string of square brackets forms a valid nested sequence.
    """
    depth = 0
    for char in string:
        if char == '[':
            depth += 1
        elif char == ']':
            depth -= 1
            if depth < 0:
                return False
        if depth > 1:
            return True
    return False