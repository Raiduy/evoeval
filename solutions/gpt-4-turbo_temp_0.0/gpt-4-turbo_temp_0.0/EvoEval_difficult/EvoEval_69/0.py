def advanced_search(lst, f):
    frequency_dict = {}
    for num in lst:
        if num > 0:
            frequency_dict[num] = frequency_dict.get(num, 0) + 1
    result = -1
    for (num, freq) in frequency_dict.items():
        if freq >= num and f % freq == 0:
            result = max(result, num)
    return result