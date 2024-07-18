def next_smallest_sorted_binary(lst):
    if len(lst) < 2:
        return None
    lst.sort(key=lambda x: (bin(x).count('1'), x))
    return lst[1]