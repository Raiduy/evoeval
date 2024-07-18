def round_and_flip(value: str) -> str:
    num = float(value[:-3])
    str_ = value[-3:]
    if num >= 0:
        num = round(num)
    else:
        num = round(num)
    return str(num) + ' ' + str_.swapcase()