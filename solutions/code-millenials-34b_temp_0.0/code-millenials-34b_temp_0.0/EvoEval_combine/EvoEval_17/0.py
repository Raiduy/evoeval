
def fibfib_search(n: int, lst: list) -> int:

    def fibfib(n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)
    fibfib_n = fibfib(n)
    max_freq = -1
    for i in lst:
        if i > 0 and lst.count(i) >= fibfib_n:
            max_freq = max(max_freq, i)
    return max_freq