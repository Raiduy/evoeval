
def prod_signs(arr):
    if not arr:
        return None
    sum_abs = sum((abs(x) for x in arr))
    prod_sign = None
    for x in arr:
        if x > 0:
            if prod_sign is None:
                prod_sign = 1
            else:
                prod_sign *= 1
        elif x < 0:
            if prod_sign is None:
                prod_sign = -1
            else:
                prod_sign *= -1
        else:
            return 0
    return sum_abs * prod_sign