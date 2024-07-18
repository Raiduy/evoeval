
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

    def to_float(val):
        if isinstance(val, str):
            val = val.replace(',', '.')
        return float(val)
    a_float = to_float(a)
    b_float = to_float(b)
    if a_float > b_float:
        return a
    elif b_float > a_float:
        return b
    else:
        return None