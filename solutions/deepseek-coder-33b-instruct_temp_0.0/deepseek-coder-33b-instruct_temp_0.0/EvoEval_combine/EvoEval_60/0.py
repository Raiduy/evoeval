
def smallest_even_triple(arr, n):
    a = [i * i - i + 1 for i in range(1, n + 1)]
    smallest_triple = None
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    if smallest_triple is None or a[i] < smallest_triple[0]:
                        smallest_triple = (a[i], a[j], a[k])
    if smallest_triple is not None:
        arr.append(smallest_triple[0])
        even_values = [(val, idx) for (idx, val) in enumerate(arr) if val % 2 == 0]
        if even_values:
            return min(even_values, key=lambda x: (x[0], x[1]))
    return []