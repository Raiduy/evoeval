
def triples_sum_to_ten(l: list):
    n = len(l)
    if n < 3:
        return False
    l.sort()
    for i in range(n - 2):
        if i > 0 and l[i] == l[i - 1]:
            continue
        j = i + 1
        k = n - 1
        while j < k:
            s = l[i] + l[j] + l[k]
            if s == 10:
                return True
            elif s < 10:
                j += 1
            else:
                k -= 1
    return False