def compare_happiness(a, b):

    def is_happy(s):
        if len(s) < 3:
            return False
        for i in range(len(s) - 2):
            if s[i] == s[i + 1] or s[i] == s[i + 2] or s[i + 1] == s[i + 2]:
                return False
        return True
    if not is_happy(a) and (not is_happy(b)):
        return None
    elif is_happy(a) and (not is_happy(b)):
        return a
    elif not is_happy(a) and is_happy(b):
        return b
    else:
        a = float(a.replace(',', '.'))
        b = float(b.replace(',', '.'))
        if a > b:
            return str(a).replace('.', ',')
        elif a < b:
            return str(b).replace('.', ',')
        else:
            return None