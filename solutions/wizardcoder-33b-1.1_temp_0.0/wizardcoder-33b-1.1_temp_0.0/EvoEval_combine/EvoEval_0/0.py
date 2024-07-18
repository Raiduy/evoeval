def compare_happiness(a, b):

    def is_happy(s):
        if len(s) < 3:
            return False
        s = s.replace(',', '.')
        for i in range(len(s) - 2):
            if s[i] != s[i + 1] and s[i] != s[i + 2] and (s[i + 1] != s[i + 2]):
                return True
        return False
    a_happy = is_happy(a)
    b_happy = is_happy(b)
    if not a_happy and (not b_happy):
        return None
    elif a_happy and (not b_happy):
        return a
    elif not a_happy and b_happy:
        return b
    else:
        a = float(a.replace(',', '.'))
        b = float(b.replace(',', '.'))
        if a > b:
            return a
        elif a < b:
            return b
        else:
            return None