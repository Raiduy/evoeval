def change_base(x: str, base: int, new_base: int) -> str:
    try:
        decimal = int(x, base)
    except ValueError:
        return 'invalid base'
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if decimal == 0:
        return '0'
    else:
        result = ''
        while decimal > 0:
            result = alphabet[decimal % new_base] + result
            decimal //= new_base
        return result