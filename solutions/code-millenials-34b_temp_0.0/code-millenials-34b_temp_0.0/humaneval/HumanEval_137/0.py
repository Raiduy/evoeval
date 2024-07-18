
def compare_one(a, b):
    # Convert to string, replace optional ',' by '.'
    a = str(a).replace(',', '.')
    b = str(b).replace(',', '.')
    # Convert to float
    a = float(a)
    b = float(b)
    # Return None if values are equal
    if a == b:
        return None
    # Return the maximum value in the original type
    elif a > b:
        return a if '.' in str(a) else int(a)
    else:
        return b if '.' in str(b) else int(b)
