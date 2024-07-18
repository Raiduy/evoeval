def round_and_flip(value: str) -> str:
    match = re.match('([-+]?\\d*\\.?\\d+)([a-zA-Z]+)', value)
    if not match:
        return 'Invalid input'
    (number_part, string_part) = match.groups()
    number = float(number_part)
    rounded_number = int(math.copysign(math.ceil(abs(number)), number))
    flipped_string = string_part.swapcase()
    return f'{rounded_number} {flipped_string}'