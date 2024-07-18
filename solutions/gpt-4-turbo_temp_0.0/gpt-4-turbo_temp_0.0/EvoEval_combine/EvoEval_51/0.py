
def modify_and_compare(a, b):

    def modify(x):
        if isinstance(x, str):
            if any((c.isalpha() for c in x)):
                return x.swapcase()
            else:
                return x[::-1]
        return x

    def is_real_number(x):
        try:
            if isinstance(x, str):
                x = x.replace(',', '.')
            float(x)
            return True
        except ValueError:
            return False
    a_modified = modify(a)
    b_modified = modify(b)
    if is_real_number(a_modified) and is_real_number(b_modified):
        a_num = float(a_modified.replace(',', '.')) if isinstance(a_modified, str) else a_modified
        b_num = float(b_modified.replace(',', '.')) if isinstance(b_modified, str) else b_modified
        if a_num > b_num:
            return a
        elif b_num > a_num:
            return b
        else:
            return None
    else:
        return b