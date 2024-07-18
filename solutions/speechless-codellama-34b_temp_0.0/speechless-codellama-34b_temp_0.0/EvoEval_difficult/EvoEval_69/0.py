def advanced_search(lst, f):
    freq = {}
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    greatest = -1
    for (num, count) in freq.items():
        if count >= num and f % count == 0 and (num > greatest):
            greatest = num
    return greatest