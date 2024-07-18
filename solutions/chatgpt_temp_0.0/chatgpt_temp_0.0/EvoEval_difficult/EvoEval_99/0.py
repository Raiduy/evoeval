def closest_integer(value, base):
    if '.' not in value:
        return value
    (integer_part, fractional_part) = value.split('.')
    decimal_integer = 0
    for i in range(len(integer_part)):
        decimal_integer += int(integer_part[-(i + 1)]) * base ** i
    decimal_fractional = 0
    for i in range(len(fractional_part)):
        decimal_fractional += int(fractional_part[i]) * base ** (-(i + 1))
    decimal_value = decimal_integer + decimal_fractional
    rounded_decimal = round(decimal_value)
    result = ''
    while rounded_decimal > 0:
        remainder = rounded_decimal % base
        result = str(remainder) + result
        rounded_decimal //= base
    if integer_part != '0':
        result = integer_part + result
    if value[0] == '-':
        result = '-' + result
    return result