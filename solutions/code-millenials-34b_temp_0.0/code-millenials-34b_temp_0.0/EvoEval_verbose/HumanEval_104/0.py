
def unique_digits(x):
    odd_digits_only = [num for num in x if all((int(digit) % 2 != 0 for digit in str(num)))]
    sorted_list = sorted(odd_digits_only)
    return sorted_list