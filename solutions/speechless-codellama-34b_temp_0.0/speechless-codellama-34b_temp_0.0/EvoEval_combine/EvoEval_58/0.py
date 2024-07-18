def max_freq_and_sum_check(lst, a, b):
    freq = {}
    max_freq = -1
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
        if freq[num] >= num and num > max_freq:
            max_freq = num
    if max_freq == -1:
        return (-1, False)
    elif a == max_freq + b or b == max_freq + a:
        return (max_freq, True)
    else:
        return (max_freq, False)