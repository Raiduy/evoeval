def compare_happiness(a, b):
    a_happy = is_happy(a)
    b_happy = is_happy(b)
    if not a_happy and (not b_happy):
        return None
    if a_happy and (not b_happy):
        return a
    if b_happy and (not a_happy):
        return b
    a_float = float(a.replace(',', '.'))
    b_float = float(b.replace(',', '.'))
    if a_float > b_float:
        return a
    elif b_float > a_float:
        return b
    else:
        return None