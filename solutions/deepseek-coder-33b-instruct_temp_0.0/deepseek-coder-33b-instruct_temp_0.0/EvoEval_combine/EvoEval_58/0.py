def max_freq_and_sum_check(lst, a, b):
    from collections import Counter
    counter = Counter(lst)
    max_freq = -1
    for (num, freq) in counter.items():
        if freq >= num and num > max_freq:
            max_freq = num
    if max_freq == -1:
        return (max_freq, False)
    else:
        return (max_freq, max_freq + min(a, b) == max(a, b))