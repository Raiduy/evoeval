
def get_common_max_triples(n, l1: list):
    a = [i * i - i + 1 for i in range(1, n + 1)]
    common_elements = sorted(list(set(a) & set(l1)))
    multiples_of_3 = [x for x in common_elements if x % 3 == 0]
    if len(multiples_of_3) == 0:
        return 0
    count = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            for k in range(j + 1, len(a)):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    return (common_elements, count)