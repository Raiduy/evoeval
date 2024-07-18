
def cycpattern_check(a , b):
    # Create a string that is twice as long as 'a' to accommodate for rotations
    a_twice = a + a
    # Check if 'b' or any of its rotations is a substring in 'a'
    for i in range(len(b)):
        # Get a rotation of 'b'
        rotated_b = b[i:] + b[:i]
        # If 'b' or any of its rotations is a substring in 'a', return True
        if rotated_b in a_twice:
            return True
    # If 'b' and all its rotations are not substrings in 'a', return False
    return False
