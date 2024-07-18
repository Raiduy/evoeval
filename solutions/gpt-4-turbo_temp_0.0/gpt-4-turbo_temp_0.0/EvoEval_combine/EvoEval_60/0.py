
def smallest_even_triple(arr, n):
    a = [i * i - i + 1 for i in range(1, n + 1)]
    smallest_sum = float('inf')
    smallest_triple = None
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    if a[i] < smallest_sum:
                        smallest_sum = a[i]
                        smallest_triple = (a[i], a[j], a[k])
    if smallest_triple:
        arr.append(smallest_triple[0])
    smallest_even = float('inf')
    index_of_smallest_even = -1
    for (i, value) in enumerate(arr):
        if value % 2 == 0 and value < smallest_even:
            smallest_even = value
            index_of_smallest_even = i
    if smallest_even != float('inf'):
        return [smallest_even, index_of_smallest_even]
    else:
        return []