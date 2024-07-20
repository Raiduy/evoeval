
def smallest_even_triple(arr, n):
    a = [i * i - i + 1 for i in range(1, n + 1)]
    smallest_triple = None
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    if smallest_triple is None or a[i] < a[smallest_triple[0]]:
                        smallest_triple = (i, j, k)
    if smallest_triple is None:
        return []
    arr.append(a[smallest_triple[0]])
    smallest_even = None
    smallest_even_index = None
    for (i, val) in enumerate(arr):
        if val % 2 == 0:
            if smallest_even is None or val < smallest_even:
                smallest_even = val
                smallest_even_index = i
    if smallest_even is None:
        return []
    return [smallest_even, smallest_even_index]