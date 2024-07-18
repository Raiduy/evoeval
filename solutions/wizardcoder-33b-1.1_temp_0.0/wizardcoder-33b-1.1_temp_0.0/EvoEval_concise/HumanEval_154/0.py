
def cycpattern_check(a, b):
    """Check if any rotation of the second word is a substring of the first word. Return True if so, else return False."""
    for i in range(len(b)):
        b = b[1:] + b[0]
        if b in a:
            return True
    return False