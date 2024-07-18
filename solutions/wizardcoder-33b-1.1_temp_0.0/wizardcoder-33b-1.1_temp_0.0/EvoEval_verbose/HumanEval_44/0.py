

def change_base(x: int, base: int) -> str:
    """
    Convert and change the numerical base of a given input number 'x' into a different base 'base'.
    """
    if x == 0:
        return '0'
    digits = []
    while x:
        digits.append(str(x % base))
        x //= base
    return ''.join(digits[::-1])