def compare_one(a, b):

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