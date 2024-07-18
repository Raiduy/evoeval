
def prod_signs(arr):
    if len(arr) == 0:
        return None
    sum_abs = sum((abs(x) for x in arr))
    sign_product = 1
    for x in arr:
        if x < 0:
            sign_product *= -1
    return sum_abs * sign_product