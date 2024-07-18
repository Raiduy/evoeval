
def prod_signs(arr):
    if not arr:
        return None

    sign_product = 1
    sum_of_magnitudes = 0

    for num in arr:
        if num > 0:
            sign_product *= 1
            sum_of_magnitudes += num
        elif num < 0:
            sign_product *= -1
            sum_of_magnitudes += abs(num)
        else:
            return 0

    return sign_product * sum_of_magnitudes
