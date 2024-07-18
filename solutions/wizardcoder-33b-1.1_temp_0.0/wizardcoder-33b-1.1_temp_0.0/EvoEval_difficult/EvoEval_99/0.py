def closest_integer(value, base):
    if '.' in value:
        (integer_part, fractional_part) = value.split('.')
        decimal_value = int(integer_part, base)
        fractional_value = 0
        for (i, digit) in enumerate(fractional_part):
            fractional_value += int(digit, base) * base ** (-(i + 1))
        decimal_value += fractional_value
        decimal_value = round(decimal_value)
        result = ''
        while decimal_value:
            result = str(decimal_value % base) + result
            decimal_value //= base
        return result
    else:
        decimal_value = int(value, base)
        return str(decimal_value)