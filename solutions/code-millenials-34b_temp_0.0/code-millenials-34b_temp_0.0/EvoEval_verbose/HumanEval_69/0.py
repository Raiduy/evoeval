
def search(lst):
    freq_dict = {}
    for num in lst:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    result = -1
    for (num, freq) in freq_dict.items():
        if num > 0 and freq >= num and (num > result):
            result = num
    return result