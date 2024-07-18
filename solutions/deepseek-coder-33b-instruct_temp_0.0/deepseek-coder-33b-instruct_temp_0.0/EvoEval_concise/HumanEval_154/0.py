
def cycpattern_check(a, b):
    """Check if any rotation of the second word is a substring of the first word. Return True if so, else return False.

    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    rotations = [b[i:] + b[:i] for i in range(len(b))]
    for rotation in rotations:
        if rotation in a:
            return True
    return False