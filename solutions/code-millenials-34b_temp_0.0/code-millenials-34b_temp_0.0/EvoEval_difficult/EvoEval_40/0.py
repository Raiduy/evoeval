def triples_sum_to_target(l: list, k: int):
    l.sort()
    count = 0
    for i in range(len(l) - 2):
        if i > 0 and l[i] == l[i - 1]:
            continue
        start = i + 1
        end = len(l) - 1
        while start < end:
            if l[i] + l[start] + l[end] == k:
                count += 1
                start += 1
                end -= 1
                while start < end and l[start] == l[start - 1]:
                    start += 1
                while start < end and l[end] == l[end + 1]:
                    end -= 1
            elif l[i] + l[start] + l[end] < k:
                start += 1
            else:
                end -= 1
    return count if count != 0 else -1