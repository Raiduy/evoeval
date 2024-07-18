def max_freq_and_sum_check(lst, a, b):
    freq = {}
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    max_freq = -1
    for (num, count) in freq.items():
        if num <= count and num > max_freq:
            max_freq = num
    if max_freq != -1:
        if a == max_freq + b or b == max_freq + a:
            return (max_freq, True)
    return (max_freq, False)