def max_freq_and_sum_check(lst, a, b):
    from collections import Counter
    freq_dict = Counter(lst)
    max_freq = -1
    for (num, freq) in freq_dict.items():
        if freq >= num and num > max_freq:
            max_freq = num
    if max_freq == -1:
        return (-1, False)
    else:
        return (max_freq, max_freq + a == b or max_freq + b == a)