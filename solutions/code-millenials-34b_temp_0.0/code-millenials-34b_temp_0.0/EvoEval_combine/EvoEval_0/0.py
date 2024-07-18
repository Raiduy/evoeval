def compare_happiness(a, b):

    def is_happy(s):
        s = s.replace(',', '.')
        try:
            float(s)
        except ValueError:
            return False
        return len(s) >= 3 and all((s[i] != s[i + 1] != s[i + 2] for i in range(len(s) - 2)))
    if not is_happy(a) and (not is_happy(b)):
        return None
    elif is_happy(a) and (not is_happy(b)):
        return a
    elif not is_happy(a) and is_happy(b):
        return b
    else:
        (a, b) = map(float, [a, b])
        if a > b:
            return str(a)
        elif a < b:
            return str(b)
        else:
            return None