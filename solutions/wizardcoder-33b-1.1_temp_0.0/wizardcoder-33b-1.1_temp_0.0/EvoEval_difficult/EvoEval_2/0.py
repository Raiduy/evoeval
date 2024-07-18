def truncate_number(number: float, digit_limit: int) -> str:
    (integer_part, decimal_part) = str(number).split('.')
    decimal_part = decimal_part[:digit_limit]
    decimal_part += '0' * (digit_limit - len(decimal_part))
    return '0.' + decimal_part