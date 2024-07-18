def max_freq_and_sum_check(lst, a, b):
    freq_dict = {}
    for num in lst:
        freq_dict[num] = freq_dict.get(num, 0) + 1
    max_freq = -1
    for (num, freq) in freq_dict.items():
        if freq >= num and num > max_freq:
            max_freq = num
    if max_freq == -1:
        return (-1, False)
    if a == max_freq + b or b == max_freq + a:
        return (max_freq, True)
    else:
        return (max_freq, False)