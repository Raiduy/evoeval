def multi_pairs_sum_to_zero(l, n):
    if n > len(l):
        return False
    else:
        l.sort()
        for i in range(len(l)):
            for j in range(i + 1, len(l)):
                if l[i] + l[j] == 0:
                    n -= 1
                    if n == 0:
                        return True
        return False