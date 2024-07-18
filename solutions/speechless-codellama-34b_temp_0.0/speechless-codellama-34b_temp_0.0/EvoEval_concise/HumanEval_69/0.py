
def search(lst):
    freq = {}
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    highest = -1
    for (num, count) in freq.items():
        if count >= num and num > highest:
            highest = num
    return highest