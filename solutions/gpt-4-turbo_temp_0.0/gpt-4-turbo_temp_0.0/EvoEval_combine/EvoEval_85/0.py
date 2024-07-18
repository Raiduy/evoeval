def next_smallest_sorted_binary(lst):
    sorted_lst = sorted(lst, key=lambda x: (bin(x).count('1'), x))
    if len(sorted_lst) < 2:
        return None
    return sorted_lst[1]