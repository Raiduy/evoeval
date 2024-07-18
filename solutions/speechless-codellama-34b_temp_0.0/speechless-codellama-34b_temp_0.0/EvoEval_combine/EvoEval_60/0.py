
def smallest_even_triple(arr, n):
    a = [i * i - i + 1 for i in range(1, n + 1)]
    triple = []
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    triple.append((a[i], a[j], a[k]))
    if not triple:
        return []
    triple.sort(key=lambda x: x[0])
    arr.append(triple[0][0])
    even_val = [x for x in arr if x % 2 == 0]
    if not even_val:
        return []
    even_val.sort()
    return [even_val[0], arr.index(even_val[0])]