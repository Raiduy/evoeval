def compare_one(a, b):
    if a == b:
        return None
    if isinstance(a, str):
        a = a.replace(',', '.')
    if isinstance(b, str):
        b = b.replace(',', '.')
    if float(a) > float(b):
        if isinstance(a, int):
            return int(a)
        elif isinstance(a, float):
            return float(a)
        else:
            return str(a)
    elif isinstance(b, int):
        return int(b)
    elif isinstance(b, float):
        return float(b)
    else:
        return str(b)