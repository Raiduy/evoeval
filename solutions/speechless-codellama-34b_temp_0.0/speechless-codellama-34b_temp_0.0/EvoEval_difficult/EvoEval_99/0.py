def closest_integer(value, base):
    if '.' in value:
        decimal_value = 0
        for (i, digit) in enumerate(reversed(value)):
            if digit == '.':
                break
            decimal_value += int(digit, base) * base ** i
        rounded_value = round(decimal_value)
        closest_integer = ''
        while rounded_value > 0:
            closest_integer = str(rounded_value % base) + closest_integer
            rounded_value //= base
        return closest_integer
    else:
        integer_value = int(value, base)
        rounded_value = round(integer_value)
        closest_integer = ''
        while rounded_value > 0:
            closest_integer = str(rounded_value % base) + closest_integer
            rounded_value //= base
        return closest_integer