
def get_common_max_triples(n, l1: list):
    a = [i * i - i + 1 for i in range(1, n + 1)]
    common_elements = sorted(set(a).intersection(l1))
    multiples_of_3 = [x for x in common_elements if x % 3 == 0]
    if not multiples_of_3:
        return (common_elements, 0)
    triples_count = 0
    for i in range(len(a) - 2):
        for j in range(i + 1, len(a) - 1):
            for k in range(j + 1, len(a)):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    triples_count += 1
    return (common_elements, triples_count)