
def compare_one(a, b):
    """
    Returns the greater of two inputs, each of which may be an integer, float, or string representing a real number. 
    If a number is expressed as a string, it could contain either '.' or ',' as the decimal point. 
    If inputs are equal, the function returns None.

    compare_one(1, 2.5) ➞ 2.5
    compare_one(1, "2,3") ➞ "2,3"
    compare_one("5,1", "6") ➞ "6"
    compare_one("1", 1) ➞ None
    """
    if isinstance(a, str) and isinstance(b, str):
        a = a.replace(',', '.')
        b = b.replace(',', '.')
    elif isinstance(a, str):
        a = a.replace(',', '.')
        a = float(a)
    elif isinstance(b, str):
        b = b.replace(',', '.')
        b = float(b)
    if a == b:
        return None
    elif a > b:
        return a
    else:
        return b