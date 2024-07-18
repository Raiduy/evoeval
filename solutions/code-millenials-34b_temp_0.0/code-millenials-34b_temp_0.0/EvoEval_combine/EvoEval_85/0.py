def next_smallest_sorted_binary(lst):
    if len(lst) < 2:
        return None

    def count_ones(n):
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count
    lst.sort(key=lambda x: (count_ones(x), x))
    return lst[1] if lst[0] != lst[1] else None