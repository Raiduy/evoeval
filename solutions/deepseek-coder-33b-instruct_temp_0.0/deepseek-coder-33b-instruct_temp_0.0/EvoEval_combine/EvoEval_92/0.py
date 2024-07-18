
def get_common_max_triples(n, l1):
    a = [i * i - i + 1 for i in range(1, n + 1)]
    common = sorted(list(set(a) & set(l1)))
    count = 0
    for i in range(len(common)):
        for j in range(i + 1, len(common)):
            for k in range(j + 1, len(common)):
                if (common[i] + common[j] + common[k]) % 3 == 0:
                    count += 1
    return (common, count)