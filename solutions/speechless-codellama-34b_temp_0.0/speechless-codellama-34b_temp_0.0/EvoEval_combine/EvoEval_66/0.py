
def find_max_triple_sum(x, y, n):
    largest_even = -1
    for i in range(x, y + 1):
        if i % 2 == 0 and i > largest_even:
            largest_even = i
    a = [i * i - i + 1 for i in range(1, n + 1)]
    max_sum = -1
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0 and a[i] + a[j] + a[k] > max_sum:
                    max_sum = a[i] + a[j] + a[k]
    if max_sum == -1:
        return -1
    if largest_even != -1:
        max_sum += largest_even
    return max_sum