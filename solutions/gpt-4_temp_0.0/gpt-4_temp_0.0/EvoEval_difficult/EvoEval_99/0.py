def closest_integer(value, base):

    def convert_to_decimal(num, base):
        num = str(num)
        decimal = 0
        for digit in num:
            decimal = base * decimal + int(digit, base)
        return decimal

    def convert_from_decimal(num, base):
        conversion = '0123456789ABCDEF'
        if num < base:
            return conversion[num]
        else:
            return convert_from_decimal(num // base, base) + conversion[num % base]
    if '.' in value:
        (integer_part, fractional_part) = value.split('.')
        decimal_value = convert_to_decimal(integer_part, base) + convert_to_decimal(fractional_part, base) / base ** len(fractional_part)
        rounded_value = round(decimal_value)
    else:
        rounded_value = convert_to_decimal(value, base)
    return convert_from_decimal(rounded_value, base)