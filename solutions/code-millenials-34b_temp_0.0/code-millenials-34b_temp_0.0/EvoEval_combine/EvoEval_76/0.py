def sort_prime_digit_sum(lst):
    modified = []
    for num in lst:
        if is_prime(num):
            modified.append(sum((int(digit) for digit in str(num))))
        else:
            modified.append(num)
    if (modified[0] + modified[-1]) % 2 == 0:
        return sorted(modified, reverse=True)
    else:
        return sorted(modified)