def change_base(x: str, base: int, new_base: int):
    try:
        base_10 = int(x, base)
    except ValueError:
        return 'invalid base'
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if base_10 == 0:
        return '0'
    else:
        result = ''
        while base_10:
            (base_10, remainder) = divmod(base_10, new_base)
            result = alphabet[remainder] + result
        return result