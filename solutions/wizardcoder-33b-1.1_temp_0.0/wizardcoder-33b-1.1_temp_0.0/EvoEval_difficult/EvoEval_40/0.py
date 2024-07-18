def triples_sum_to_target(l: list, k: int):
    l.sort()
    count = 0
    for i in range(len(l) - 2):
        left = i + 1
        right = len(l) - 1
        while left < right:
            if l[i] + l[left] + l[right] == k:
                count += 1
                left += 1
                right -= 1
            elif l[i] + l[left] + l[right] < k:
                left += 1
            else:
                right -= 1
    return count if count > 0 else -1