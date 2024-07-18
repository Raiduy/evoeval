
def find_max_triple_sum(x, y, n):
    largest_even = -1
    for num in range(x, y + 1):
        if num % 2 == 0 and num > largest_even:
            largest_even = num
    if largest_even == -1:
        return -1
    a = [i * i - i + 1 for i in range(1, n + 1)]
    largest_sum = -1
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                triple_sum = a[i] + a[j] + a[k]
                if triple_sum % 3 == 0 and triple_sum > largest_sum:
                    largest_sum = triple_sum
    largest_sum += largest_even
    return largest_sum