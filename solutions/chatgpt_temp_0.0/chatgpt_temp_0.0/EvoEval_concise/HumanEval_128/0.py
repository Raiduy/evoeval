
def prod_signs(arr):
    if len(arr) == 0:
        return None
    product = 1
    sum_abs = 0
    for num in arr:
        product *= 1 if num > 0 else -1 if num < 0 else 0
        sum_abs += abs(num)
    return product * sum_abs