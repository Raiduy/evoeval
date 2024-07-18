
def modp_count(arr, n: int, p: int) -> int:
    mod_2pn = pow(2, n, p)
    count = 0
    for num in arr:
        sum_digits = sum((int(digit) for digit in str(abs(num))))
        if num < 0:
            sum_digits = mod_2pn - sum_digits
        if sum_digits > mod_2pn:
            count += 1
    return count