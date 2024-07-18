def compare_happiness(a, b):

    def is_happy(s):
        if len(s) < 3:
            return False
        for i in range(len(s) - 2):
            if s[i] == s[i + 1] or s[i] == s[i + 2] or s[i + 1] == s[i + 2]:
                return False
        return True
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