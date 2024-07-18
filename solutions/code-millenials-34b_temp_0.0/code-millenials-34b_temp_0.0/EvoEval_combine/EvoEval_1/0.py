def round_and_flip(value: str) -> str:
    (num, string) = (float(value[:-3]), value[-3:])
    rounded_num = round(num)
    flipped_string = string.swapcase()
    return str(rounded_num) + ' ' + flipped_string