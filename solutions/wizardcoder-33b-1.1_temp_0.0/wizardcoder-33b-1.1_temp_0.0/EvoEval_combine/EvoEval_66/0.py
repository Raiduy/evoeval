
def find_max_triple_sum(x, y, n):
    max_even = -1
    for i in range(y, x - 1, -1):
        if i % 2 == 0:
            max_even = i
            break
    if max_even == -1:
        return -1
    a = [i * i - i + 1 for i in range(1, n + 1)]
    a.sort(reverse=True)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    return a[i] + a[j] + a[k] + max_even
    return -1