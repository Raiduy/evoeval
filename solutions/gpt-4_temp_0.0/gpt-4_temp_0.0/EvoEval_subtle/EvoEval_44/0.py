

def change_base(x: int, base: int) -> int:
    if x == 0:
        return 0
    digits = []
    while x:
        digits.append(int(x % base))
        x //= base
    digits = digits[::-1]
    return int(''.join(map(str, digits)))