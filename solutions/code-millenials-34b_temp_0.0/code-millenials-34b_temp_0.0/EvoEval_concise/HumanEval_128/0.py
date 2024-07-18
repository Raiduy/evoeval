
def prod_signs(arr):
    if len(arr) == 0:
        return None
    else:
        result = 0
        for num in arr:
            if num > 0:
                result += num * 1
            elif num < 0:
                result += abs(num) * -1
            else:
                result += abs(num) * 0
        return result