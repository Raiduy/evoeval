
def modify_and_compare(a, b):
    if isinstance(a, str) and any((char.isalpha() for char in a)) or (isinstance(b, str) and any((char.isalpha() for char in b))):
        a = a.lower() if isinstance(a, str) and any((char.isupper() for char in a)) else a
        b = b.lower() if isinstance(b, str) and any((char.isupper() for char in b)) else b
        a = a.upper() if isinstance(a, str) and any((char.islower() for char in a)) else a
        b = b.upper() if isinstance(b, str) and any((char.islower() for char in b)) else b
    else:
        a = a[::-1] if isinstance(a, str) else a
        b = b[::-1] if isinstance(b, str) else b
    real_number_a = True
    real_number_b = True
    try:
        float(a.replace(',', '.'))
    except ValueError:
        real_number_a = False
    try:
        float(b.replace(',', '.'))
    except ValueError:
        real_number_b = False
    if real_number_a and real_number_b:
        if float(a.replace(',', '.')) > float(b.replace(',', '.')):
            return a
        elif float(a.replace(',', '.')) < float(b.replace(',', '.')):
            return b
        else:
            return None
    else:
        return b