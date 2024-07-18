
def search(lst):
    freq = {}
    for i in lst:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    for i in range(1, max(freq.keys()) + 1):
        if i in freq and freq[i] >= i:
            return i
    return -1