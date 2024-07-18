
def prod_signs(arr):
    if not arr:
        return None
    else:
        sum = 0
        for num in arr:
            sum += abs(num) * (1 if num > 0 else -1 if num < 0 else 0)
        return sum