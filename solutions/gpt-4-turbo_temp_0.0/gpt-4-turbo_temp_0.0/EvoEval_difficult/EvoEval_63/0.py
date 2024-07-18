def customFibFib(n: int, startSequence: list, p: int):
    if n < 3:
        return startSequence[n]
    seq = startSequence + [0] * (n - 2)
    for i in range(3, n + 1):
        seq[i] = seq[i - 1] + seq[i - 2] + seq[i - 3]
        if seq[i] > p:
            return 'Limit Exceeded'
    return seq[n]