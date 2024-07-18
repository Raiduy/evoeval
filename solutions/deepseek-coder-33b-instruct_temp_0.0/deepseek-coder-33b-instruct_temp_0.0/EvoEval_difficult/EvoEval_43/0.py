def multi_pairs_sum_to_zero(l, n):
    if n > len(l):
        return False
    zero_sum_set = set()
    for i in range(len(l)):
        if l[i] in zero_sum_set:
            return True
        else:
            zero_sum_set.add(-l[i])
    return False