def multi_pairs_sum_to_zero(l, n):
    if n > len(l):
        return False
    else:
        pairs = []
        for i in range(len(l)):
            for j in range(i + 1, len(l)):
                if l[i] + l[j] == 0:
                    pairs.append((l[i], l[j]))
        return len(set(pairs)) == n