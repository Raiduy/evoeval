def round_and_flip(value: str) -> str:
    (num_str, str_part) = value.split(maxsplit=1)
    num = float(num_str)
    rounded_num = int(num + 0.5) if num > 0 else int(num - 0.5)
    flipped_str = str_part.swapcase()
    return f'{rounded_num} {flipped_str}'