
def smallest_even_triple(arr, n):
    a = [i * i - i + 1 for i in range(1, n + 1)]
    smallest_triple = None
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            for k in range(j + 1, len(a)):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    if smallest_triple is None or a[i] < smallest_triple[0]:
                        smallest_triple = (a[i], a[j], a[k])
    if smallest_triple is not None:
        arr.append(smallest_triple[0])
    smallest_even_value = None
    smallest_even_index = None
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            if smallest_even_value is None or arr[i] < smallest_even_value:
                smallest_even_value = arr[i]
                smallest_even_index = i
    if smallest_even_value is not None:
        return [smallest_even_value, smallest_even_index]
    else:
        return []