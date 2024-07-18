
def will_it_fly(q, w):
    """
    Returns True if list q is palindromic and the sum of its elements is less or equal to w, False otherwise.
    """
    if q == q[::-1] and sum(q) <= w:
        return True
    else:
        return False