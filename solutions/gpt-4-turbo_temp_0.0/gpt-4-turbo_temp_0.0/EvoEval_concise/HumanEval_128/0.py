
def prod_signs(arr):
    """
    For a given array arr of integers, return the sum of absolute values of integers multiplied by 
    the product of their signs (represented by 1, -1, or 0). If the array is empty, return None.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    """
    if not arr:
        return None
    sign_product = 1
    for num in arr:
        if num > 0:
            sign_product *= 1
        elif num < 0:
            sign_product *= -1
        else:
            sign_product = 0
            break
    result = sum((abs(num) for num in arr)) * sign_product
    return result