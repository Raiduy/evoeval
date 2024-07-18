def compare_one(a, b):
    a = float(str(a).replace(',', '.'))
    b = float(str(b).replace(',', '.'))
    if a > b:
        return a if isinstance(a, str) else b
    elif b > a:
        return b if isinstance(b, str) else a
    else:
        return None