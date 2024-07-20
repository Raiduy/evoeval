
def prod_signs(arr):
    if not arr:
        return None
    product_of_signs = 1
    sum_of_abs_values = 0
    for num in arr:
        if num > 0:
            product_of_signs *= 1
            sum_of_abs_values += num
        elif num < 0:
            product_of_signs *= -1
            sum_of_abs_values += abs(num)
        else:
            product_of_signs *= 0
            sum_of_abs_values += 0
    return sum_of_abs_values * product_of_signs