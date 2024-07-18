
def fibfib_search(n: int, lst: list) -> int:

    def fibfib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)
    freq = {}
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    fibfib_n = fibfib(n)
    for num in sorted(freq.keys(), reverse=True):
        if num > 0 and freq[num] >= fibfib_n:
            return num
    return -1