
def smallest_even_triple(arr, n):
    a = [i * i - i + 1 for i in range(1, n + 1)]
    smallest_triple = None
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            for k in range(j + 1, len(a)):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    if smallest_triple is None or a[i] < smallest_triple[0]:
                        smallest_triple = [a[i], a[j], a[k]]
    if smallest_triple is not None:
        arr.append(smallest_triple[0])
    even_numbers = [num for num in arr if num % 2 == 0]
    if even_numbers:
        return [min(even_numbers), arr.index(min(even_numbers))]
    else:
        return []