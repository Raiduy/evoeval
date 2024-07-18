def nature_sequence_generator(n, a, b):
    sequence = [a, b]
    next_add = 1
    while len(sequence) < n:
        next_element = sequence[-1] + sequence[-2] + next_add
        sequence.append(next_element)
        next_add += 1
    for i in range(len(sequence)):
        if is_prime(sequence[i]):
            sequence[i] = 'prime'
    return sequence