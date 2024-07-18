
def will_it_fly(q, w):
    """
    Returns True if list q is palindromic and the sum of its elements is less or equal to w, False otherwise.

    Example:
    will_it_fly([1, 2], 5) ➞ False 

    will_it_fly([3, 2, 3], 1) ➞ False 

    will_it_fly([3, 2, 3], 9) ➞ True  

    will_it_fly([3], 5) ➞ True  
    """
    if q != q[::-1]:
        return False
    if sum(q) > w:
        return False
    return True