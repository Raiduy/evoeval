def change_base(x: int, base: int) -> str:
    if x == 0:
        return '0'
    nums = []
    while x:
        (x, rem) = divmod(x, base)
        nums.append(str(rem))
    return ''.join(reversed(nums))