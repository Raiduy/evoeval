def round_and_flip(value: str) -> str:
    (num_str, str_part) = value.split('.')
    num_str += '.' + str_part
    num = round(float(num_str))
    str_part = str_part.swapcase()
    return str(int(num)) + ' ' + str_part