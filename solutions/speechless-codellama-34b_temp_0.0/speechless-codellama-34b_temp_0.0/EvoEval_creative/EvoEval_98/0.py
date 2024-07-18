def nature_sequence_generator(n, a, b):
    sequence = [a, b]
    for i in range(2, n):
        next_num = sequence[i - 1] + sequence[i - 2] + 1
        sequence.append(next_num)
    for i in range(len(sequence)):
        if is_prime(sequence[i]):
            sequence[i] = 'prime'
    return sequence