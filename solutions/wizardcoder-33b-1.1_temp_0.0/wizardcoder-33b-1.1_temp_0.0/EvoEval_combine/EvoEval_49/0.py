
def modp_count(arr, n: int, p: int):
    power_mod = pow(2, n, p)

    def sum_of_digits(num):
        return sum((int(digit) for digit in str(abs(num))))
    count = sum((sum_of_digits(num) > power_mod for num in arr))
    return count