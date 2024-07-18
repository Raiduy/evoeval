def truncate_number(number: float, digit_limit: int) -> str:
    decimal_part = number - int(number)
    decimal_as_str = '{:.2f}'.format(decimal_part)[2:]
    if len(decimal_as_str) < digit_limit:
        decimal_as_str += '0' * (digit_limit - len(decimal_as_str))
    return decimal_as_str