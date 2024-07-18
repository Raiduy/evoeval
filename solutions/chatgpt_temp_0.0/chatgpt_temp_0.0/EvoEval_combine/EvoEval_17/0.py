
def fibfib_search(n: int, lst: list) -> int:

    def fibfib(m: int) -> int:
        if m == 0 or m == 1:
            return 0
        elif m == 2:
            return 1
        else:
            return fibfib(m - 1) + fibfib(m - 2) + fibfib(m - 3)
    fibfib_n = fibfib(n)
    freq_dict = {}
    for num in lst:
        if num > 0:
            freq_dict[num] = freq_dict.get(num, 0) + 1
    max_num = -1
    for (num, freq) in freq_dict.items():
        if freq >= fibfib_n and num > max_num:
            max_num = num
    return max_num