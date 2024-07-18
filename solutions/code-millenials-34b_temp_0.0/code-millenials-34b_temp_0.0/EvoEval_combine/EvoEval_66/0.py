
def find_max_triple_sum(x, y, n):
    largest_even = -1
    for i in range(y, x - 1, -1):
        if i % 2 == 0:
            largest_even = i
            break
    a = [i * i - i + 1 for i in range(1, n + 1)]
    a.sort()
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    return largest_even + a[i] + a[j] + a[k]
    return -1