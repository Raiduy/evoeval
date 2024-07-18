
def fibfib_search(n: int, lst: list) -> int:
    fibfib = [0, 0, 1]
    for i in range(3, n + 1):
        fibfib.append(fibfib[i - 1] + fibfib[i - 2] + fibfib[i - 3])
    freq = {}
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    for num in sorted(freq.keys(), reverse=True):
        if freq[num] >= fibfib[n]:
            return num
    return -1