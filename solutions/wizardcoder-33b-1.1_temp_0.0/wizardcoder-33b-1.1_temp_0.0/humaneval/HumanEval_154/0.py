
def cycpattern_check(a, b):
    # Generate all rotations of b
    rotations = [b[i:] + b[:i] for i in range(len(b))]

    # Check if any rotation is a substring of a
    for rotation in rotations:
        if rotation in a:
            return True

    return False
