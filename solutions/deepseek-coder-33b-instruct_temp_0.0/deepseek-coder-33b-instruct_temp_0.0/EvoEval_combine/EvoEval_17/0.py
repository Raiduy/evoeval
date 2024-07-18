
def fibfib_search(n: int, lst: list) -> int:

    def fibfib(n: int) -> int:
        if n == 0 or n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)
    freq_dict = {}
    for num in lst:
        if num > 0:
            freq_dict[num] = freq_dict.get(num, 0) + 1
    for num in sorted(freq_dict.keys(), reverse=True):
        if freq_dict[num] >= fibfib(n):
            return num
    return -1