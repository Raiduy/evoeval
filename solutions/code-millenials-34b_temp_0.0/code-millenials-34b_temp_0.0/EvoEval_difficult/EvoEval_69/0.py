def advanced_search(lst, f):
    from collections import Counter
    c = Counter(lst)
    for i in range(max(c), 0, -1):
        if c[i] >= i and f % i == 0:
            return i
    return -1