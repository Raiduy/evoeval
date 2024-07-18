def compare_happiness(a, b):

    def is_happy(s):
        if len(s) < 3:
            return False
        for i in range(len(s) - 2):
            if s[i] == s[i + 1] or s[i] == s[i + 2] or s[i + 1] == s[i + 2]:
                return False
        return True
    if is_happy(a) and is_happy(b):
        a_num = float(a.replace(',', '.'))
        b_num = float(b.replace(',', '.'))
        if a_num > b_num:
            return a
        elif b_num > a_num:
            return b
        else:
            return None
    elif is_happy(a):
        return a
    elif is_happy(b):
        return b
    else:
        return None