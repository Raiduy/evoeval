
def prod_signs(arr):
    if not arr:
        return None
    sum_abs = 0
    sign_product = 1
    for num in arr:
        sum_abs += abs(num)
        if num == 0:
            sign_product = 0
            break
        elif num < 0:
            sign_product *= -1
    return sum_abs * sign_product