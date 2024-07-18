def closest_integer(value, base):

    def to_decimal(value, base):
        digits = '0123456789ABCDEF'
        decimal_value = 0
        for (i, digit) in enumerate(reversed(value)):
            if digit in digits:
                decimal_value += digits.index(digit) * base ** i
        return decimal_value

    def from_decimal(number, base):
        digits = '0123456789ABCDEF'
        if number == 0:
            return '0'
        elif number < 0:
            return '-' + from_decimal(-number, base)
        result = ''
        while number:
            result = digits[number % base] + result
            number //= base
        return result
    parts = value.split('.')
    whole_part = parts[0]
    fractional_part = '0.' + parts[1] if len(parts) > 1 else '0'
    whole_decimal = to_decimal(whole_part, base)
    if fractional_part != '0':
        fractional_decimal = 0
        for (i, digit) in enumerate(fractional_part[2:], start=1):
            if digit in '0123456789ABCDEF':
                fractional_decimal += int(digit, 16) / base ** i
        total_decimal = whole_decimal + fractional_decimal
        rounded_decimal = int(total_decimal + (0.5 if total_decimal > 0 else -0.5))
    else:
        rounded_decimal = whole_decimal
    return from_decimal(rounded_decimal, base)