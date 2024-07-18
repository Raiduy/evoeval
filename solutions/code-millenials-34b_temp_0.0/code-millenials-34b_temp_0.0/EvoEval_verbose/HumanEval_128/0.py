
def prod_signs(arr):
    if len(arr) == 0:
        return None
    else:
        sum_abs = sum([abs(x) for x in arr])
        prod_sign = 1
        for x in arr:
            if x < 0:
                prod_sign *= -1
            elif x > 0:
                prod_sign *= 1
        return sum_abs * prod_sign