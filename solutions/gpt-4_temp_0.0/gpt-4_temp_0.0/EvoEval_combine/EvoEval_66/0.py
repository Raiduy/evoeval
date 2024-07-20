
def find_max_triple_sum(x, y, n):
    largest_even = -1
    for i in range(y, x - 1, -1):
        if i % 2 == 0:
            largest_even = i
            break
    a = [i * i - i + 1 for i in range(1, n + 1)]
    triple_sum = -1
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                current_sum = a[i] + a[j] + a[k]
                if current_sum % 3 == 0 and current_sum > triple_sum:
                    triple_sum = current_sum
    if triple_sum == -1:
        return -1
    if largest_even == -1:
        return triple_sum
    return triple_sum + largest_even