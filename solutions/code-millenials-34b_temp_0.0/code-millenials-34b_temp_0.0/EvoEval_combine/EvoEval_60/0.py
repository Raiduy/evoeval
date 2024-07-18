
def smallest_even_triple(arr, n):
    a = [i * i - i + 1 for i in range(1, n + 1)]
    triple = [float('inf'), float('inf'), float('inf')]
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            for k in range(j + 1, len(a)):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    if a[i] < triple[0]:
                        triple = [a[i], a[j], a[k]]
    arr.append(triple[0])
    even_val = []
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            even_val.append([arr[i], i])
    if even_val:
        even_val.sort(key=lambda x: (x[0], x[1]))
        return even_val[0]
    else:
        return []