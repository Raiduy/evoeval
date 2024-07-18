def sorted_happy_strings(lst):
    """Filter, sort, and return happy strings from the list."""
    filtered_lst = [s for s in lst if is_happy(s) and len(s) % 2 == 0]
    sorted_lst = sorted(filtered_lst, key=lambda x: (len(x), x))
    return sorted_lst