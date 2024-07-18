
def unique_digits(x):
    filtered_list = []
    for num in x:
        num_str = str(num)
        if any((int(digit) % 2 == 0 for digit in num_str)):
            continue
        filtered_list.append(num)
    filtered_list.sort()
    return filtered_list