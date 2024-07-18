def multi_pairs_sum_to_zero(l, n):
    if n > len(l):
        return False
    else:
        for i in range(len(l)):
            for j in range(i + 1, len(l)):
                if l[i] + l[j] == 0:
                    l.pop(j)
                    l.pop(i)
                    return multi_pairs_sum_to_zero(l, n - 1)
        return False