
def cycpattern_check(a, b):
    """Check if any rotation of the second word is a substring of the first word. Return True if so, else return False.

    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i:] + a[:i] == b:
            return True
    return False