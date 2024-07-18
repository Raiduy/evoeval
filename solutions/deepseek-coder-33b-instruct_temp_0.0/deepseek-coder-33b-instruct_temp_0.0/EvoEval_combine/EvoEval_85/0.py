def next_smallest_sorted_binary(lst):
    lst = [(bin(i).count('1'), i) for i in lst]
    lst.sort()
    return lst[1][1] if len(lst) > 1 else None