
def modify_and_compare(a, b):
    if isinstance(a, str) and any((char.isalpha() for char in a)):
        if a.isupper():
            a = a.lower()
        else:
            a = a.upper()
    elif isinstance(a, str):
        a = a[::-1]
    if isinstance(b, str) and any((char.isalpha() for char in b)):
        if b.isupper():
            b = b.lower()
        else:
            b = b.upper()
    elif isinstance(b, str):
        b = b[::-1]
    try:
        a = float(a.replace(',', '.'))
    except ValueError:
        pass
    try:
        b = float(b.replace(',', '.'))
    except ValueError:
        pass
    if isinstance(a, float) and isinstance(b, float):
        if a > b:
            return a
        elif a < b:
            return b
        else:
            return None
    elif isinstance(a, float):
        return a
    else:
        return b