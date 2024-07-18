def triples_sum_to_target(l: list, k: int):
    l.sort()
    count = 0
    for i in range(len(l) - 2):
        left = i + 1
        right = len(l) - 1
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
    if count == 0:
        return -1
    else:
        return count