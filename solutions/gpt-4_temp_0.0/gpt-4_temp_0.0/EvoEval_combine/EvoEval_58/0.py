def max_freq_and_sum_check(lst, a, b):
    from collections import Counter
    count = Counter(lst)
    max_freq = -1
    for (num, freq) in count.items():
        if freq >= num and num > max_freq:
            max_freq = num
    if max_freq == -1:
        return (-1, False)
    else:
        return (max_freq, a == max_freq + b or b == max_freq + a)