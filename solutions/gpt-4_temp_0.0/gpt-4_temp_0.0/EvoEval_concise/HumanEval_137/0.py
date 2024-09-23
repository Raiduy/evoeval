
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
    a_float = float(str(a).replace(',', '.'))
    b_float = float(str(b).replace(',', '.'))
    if a_float > b_float:
        return a
    elif a_float < b_float:
        return b
    else:
        return None