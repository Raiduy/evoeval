
def get_common_max_triples(n, l1):
    a = [i * i - i + 1 for i in range(1, n + 1)]
    common_elements = sorted(list(set(a) & set(l1)))
    if not any((x % 3 == 0 for x in common_elements)):
        return 0
    count = 0
    for i in range(len(common_elements)):
        for j in range(i + 1, len(common_elements)):
            for k in range(j + 1, len(common_elements)):
                if (common_elements[i] + common_elements[j] + common_elements[k]) % 3 == 0:
                    count += 1
    return (common_elements, count)