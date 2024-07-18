def max_freq_and_sum_check(lst, a, b):
    max_freq = -1
    for num in set(lst):
        if lst.count(num) >= num and num > max_freq:
            max_freq = num
    if max_freq == -1:
        return (-1, False)
    else:
        return (max_freq, a == max_freq + b or b == max_freq + a)