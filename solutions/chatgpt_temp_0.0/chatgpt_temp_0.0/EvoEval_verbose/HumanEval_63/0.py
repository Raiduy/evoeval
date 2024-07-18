
def fibfib(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fibfib_seq = [0, 0, 1]
        for i in range(3, n + 1):
            fibfib_seq.append(fibfib_seq[i - 1] + fibfib_seq[i - 2] + fibfib_seq[i - 3])
        return fibfib_seq[n]