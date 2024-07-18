def closest_integer(value, base):
    (integer_part, fractional_part) = value.split('.') if '.' in value else (value, '0')
    decimal_value = int(integer_part, base)
    if fractional_part:
        decimal_value += int(fractional_part, base) / base ** len(fractional_part)
    rounded_value = round(decimal_value)
    if rounded_value < 0:
        sign = '-'
        rounded_value = -rounded_value
    else:
        sign = ''
    result = ''
    while rounded_value:
        (rounded_value, remainder) = divmod(rounded_value, base)
        result = str(remainder) + result
    return sign + result