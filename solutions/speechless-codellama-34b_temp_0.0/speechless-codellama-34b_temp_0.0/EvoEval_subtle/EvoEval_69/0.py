
def search(lst):
    freq = {}
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    for num in lst:
        if freq[num] >= num and num > 0:
            return num
    return -1