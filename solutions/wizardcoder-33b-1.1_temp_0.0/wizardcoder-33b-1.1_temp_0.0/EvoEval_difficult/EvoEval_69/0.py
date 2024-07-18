def advanced_search(lst, f):
    freq_dict = {}
    for num in lst:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    sorted_dict = dict(sorted(freq_dict.items(), reverse=True))
    for (num, freq) in sorted_dict.items():
        if f % freq == 0 and freq >= num:
            return num
    return -1