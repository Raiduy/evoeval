def next_smallest_sorted_binary(lst):
    lst.sort(key=lambda x: (bin(x).count('1'), x))
    return lst[1] if len(lst) > 1 else None