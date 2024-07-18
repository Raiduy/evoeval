def sort_even_odd(l: list, m: list):
    l_with_indices = [(val, idx) for (idx, val) in enumerate(l)]
    even_indices = [tup for tup in l_with_indices if tup[1] % 2 == 0]
    even_indices.sort(key=lambda x: m.index(x[0]) if x[0] in m else len(m))
    result = [None] * len(l)
    for i in range(0, len(l), 2):
        result[i] = l[i]
    for (i, tup) in enumerate(even_indices):
        result[2 * i + 1] = tup[0]
    return result