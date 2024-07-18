def customFibFib(n: int, startSequence: list, p: int):
    if n < 3:
        return startSequence[n]
    else:
        sequence = startSequence
        for i in range(3, n + 1):
            next_element = sequence[i - 1] + sequence[i - 2] + sequence[i - 3]
            if next_element > p:
                return 'Limit Exceeded'
            sequence.append(next_element)
        return sequence[n]