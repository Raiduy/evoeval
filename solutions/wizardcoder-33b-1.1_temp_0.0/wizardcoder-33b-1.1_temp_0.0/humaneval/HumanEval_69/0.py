
def search(lst):
    from collections import Counter
    count = Counter(lst)
    for num in sorted(count.keys(), reverse=True):
        if num <= count[num]:
            return num
    return -1
