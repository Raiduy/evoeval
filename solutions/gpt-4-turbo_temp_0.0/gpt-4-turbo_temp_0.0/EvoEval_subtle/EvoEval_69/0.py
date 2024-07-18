
def search(lst):
    from collections import Counter
    freq = Counter(lst)
    smallest_int = float('inf')
    for (num, count) in freq.items():
        if num <= count:
            smallest_int = min(smallest_int, num)
    return smallest_int if smallest_int != float('inf') else -1