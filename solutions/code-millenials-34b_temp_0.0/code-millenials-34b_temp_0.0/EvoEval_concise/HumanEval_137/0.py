
def compare_one(a, b):
    a = float(str(a).replace(',', '.'))
    b = float(str(b).replace(',', '.'))
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return None