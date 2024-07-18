
def modify_and_compare(a, b):
    if isinstance(a, str):
        if any((c.isalpha() for c in a)):
            a = a.swapcase()
        else:
            a = a[::-1]
    if isinstance(b, str):
        if any((c.isalpha() for c in b)):
            b = b.swapcase()
        else:
            b = b[::-1]
    try:
        a = float(a.replace(',', '.'))
        b = float(b.replace(',', '.'))
    except ValueError:
        pass
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return None