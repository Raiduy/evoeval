def customFibFib(n: int, startSequence: list, p: int):
    if n < 3:
        return startSequence[n]
    sequence = startSequence[:]
    for i in range(3, n + 1):
        next_value = sequence[i - 1] + sequence[i - 2] + sequence[i - 3]
        if next_value > p:
            return 'Limit Exceeded'
        sequence.append(next_value)
    return sequence[n]