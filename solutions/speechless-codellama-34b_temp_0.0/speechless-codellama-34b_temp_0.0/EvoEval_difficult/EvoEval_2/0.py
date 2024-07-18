def truncate_number(number: float, digit_limit: int) -> str:
    decimals = str(number).split('.')[1]
    if len(decimals) > digit_limit:
        decimals = decimals[:digit_limit]
    else:
        decimals = decimals.ljust(digit_limit, '0')
    return f'0.{decimals}'