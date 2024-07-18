
def prod_signs(arr):
    if len(arr) == 0:
        return None
    else:
        sum_abs = sum((abs(x) for x in arr))
        prod_signs = None
        for x in arr:
            if x < 0:
                if prod_signs is None:
                    prod_signs = -1
                else:
                    prod_signs *= -1
            elif x > 0:
                if prod_signs is None:
                    prod_signs = 1
            else:
                prod_signs = 0
                break
        if prod_signs is not None:
            return sum_abs * prod_signs
        else:
            return None