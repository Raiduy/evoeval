def next_smallest_sorted_binary(lst):
    if len(lst) < 2:
        return None

    def count_ones(num):
        return bin(num).count('1')
    sorted_lst = sorted(lst, key=lambda x: (count_ones(x), x))
    if len(sorted_lst) < 2:
        return None
    return sorted_lst[1]