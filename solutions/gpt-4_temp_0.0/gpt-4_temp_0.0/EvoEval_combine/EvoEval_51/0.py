
def modify_and_compare(a, b):

    def convert(s):
        if s.isnumeric():
            return s[::-1]
        else:
            return s.swapcase()

    def to_real(s):
        try:
            return float(s.replace(',', '.'))
        except ValueError:
            return s
    (a, b) = map(convert, map(str, (a, b)))
    (a_real, b_real) = map(to_real, (a, b))
    if isinstance(a_real, float) and isinstance(b_real, float):
        if a_real > b_real:
            return a if isinstance(a, type(a_real)) else a_real
        elif a_real < b_real:
            return b if isinstance(b, type(b_real)) else b_real
        else:
            return None
    else:
        return b