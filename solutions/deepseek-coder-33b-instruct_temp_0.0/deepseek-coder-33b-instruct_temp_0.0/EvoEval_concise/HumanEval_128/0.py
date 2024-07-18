
def prod_signs(arr):
    if not arr:
        return None
    product = 1
    sum_abs = 0
    for num in arr:
        product *= (num > 0) - (num < 0)
        sum_abs += abs(num)
    return product * sum_abs