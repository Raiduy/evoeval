
def modp_count(arr, n: int, p: int):
    twon_mod_p = pow(2, n, p)
    count = 0
    for num in arr:
        if num < 0:
            num = -num
            first_digit = -1
        else:
            first_digit = 1
        digit_sum = sum((int(digit) for digit in str(num)))
        if digit_sum > twon_mod_p:
            count += first_digit
    return count