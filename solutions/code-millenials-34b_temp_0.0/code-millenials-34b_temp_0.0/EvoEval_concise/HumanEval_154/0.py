
def cycpattern_check(a, b):
    """Check if any rotation of the second word is a substring of the first word. Return True if so, else return False."""
    for i in range(len(b)):
        if b in a * 2:
            return True
        else:
            b = b[-1] + b[:-1]
    return False