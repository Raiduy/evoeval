
def cycpattern_check(a, b):
    """
    Checks if the second word or any of its rotations is a substring in the first word.
    """
    # Concatenate the second word with itself to account for all possible rotations
    b_rotated = b * 2
    
    # Check if the first word contains the second word or any of its rotations
    return b in b_rotated and b_rotated in a * 2
