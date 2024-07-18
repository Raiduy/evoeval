
def search(lst):
    from collections import Counter
    counter = Counter(lst)
    for (num, freq) in sorted(counter.items()):
        if num == freq:
            return num
        elif num < freq:
            return -1
    return -1