
def cycpattern_check(a, b):
    """Check if any rotation of the second word is a substring of the first word. Return True if so, else return False."""
    a_doubled = a + a
    return b in a_doubled