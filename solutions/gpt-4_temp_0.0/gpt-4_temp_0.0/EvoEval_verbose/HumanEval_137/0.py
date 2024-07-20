def compare_one(a, b):
    a_float = float(str(a).replace(',', '.'))
    b_float = float(str(b).replace(',', '.'))
    if a_float > b_float:
        return a
    elif a_float < b_float:
        return b
    else:
        return None