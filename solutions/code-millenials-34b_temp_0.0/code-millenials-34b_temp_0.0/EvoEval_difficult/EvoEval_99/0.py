def closest_integer(value, base):

    def char_to_int(c):
        if '0' <= c <= '9':
            return int(c)
        elif 'A' <= c <= 'F':
            return 10 + ord(c) - ord('A')
        elif 'a' <= c <= 'f':
            return 10 + ord(c) - ord('a')

    def int_to_char(i):
        if 0 <= i <= 9:
            return str(i)
        elif 10 <= i <= 15:
            return chr(i - 10 + ord('A'))
    if '.' in value:
        (integer, fractional) = value.split('.')
        integer = int(integer, base)
        fractional = int(fractional, base) / base ** len(fractional)
        value = integer + fractional
        if value >= 0:
            value = int(value + 0.5)
        else:
            value = int(value - 0.5)
        return str(value)
    value = int(value, base)
    return str(value)