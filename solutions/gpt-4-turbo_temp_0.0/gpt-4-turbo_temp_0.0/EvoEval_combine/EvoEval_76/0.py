def sort_prime_digit_sum(lst):
    """
    Modify and sort the list as per the given conditions.
    """
    modified_list = [digit_sum(item) if is_prime(item) else item for item in lst]
    if len(modified_list) > 0 and (modified_list[0] + modified_list[-1]) % 2 == 0:
        modified_list.sort(reverse=True)
    else:
        modified_list.sort()
    return modified_list