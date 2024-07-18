def triples_sum_to_target(l: list, k: int):
    n = len(l)
    if n < 3:
        return -1
    l.sort()
    count = 0
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            current_sum = l[i] + l[left] + l[right]
            if current_sum == k:
                count += 1
                left += 1
                right -= 1
            elif current_sum < k:
                left += 1
            else:
                right -= 1
    return count if count > 0 else -1