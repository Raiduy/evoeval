
def find_max_triple_sum(x, y, n):
    largest_even = -1
    for num in range(y, x - 1, -1):
        if num % 2 == 0:
            largest_even = num
            break
    if largest_even == -1:
        return -1
    a = [i * i - i + 1 for i in range(1, n + 1)]
    a.sort(reverse=True)
    max_sum = -1
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    max_sum = a[i] + a[j] + a[k]
                    break
            if max_sum != -1:
                break
        if max_sum != -1:
            break
    if max_sum == -1:
        return -1
    return max_sum + largest_even