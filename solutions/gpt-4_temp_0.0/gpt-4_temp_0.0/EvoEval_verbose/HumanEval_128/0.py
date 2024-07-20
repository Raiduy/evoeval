
def prod_signs(arr):
    if len(arr) == 0:
        return None
    sum_abs = sum((abs(x) for x in arr))
    prod_signs = 1
    for x in arr:
        if x > 0:
            prod_signs *= 1
        elif x < 0:
            prod_signs *= -1
        else:
            prod_signs *= 0
    return sum_abs * prod_signs