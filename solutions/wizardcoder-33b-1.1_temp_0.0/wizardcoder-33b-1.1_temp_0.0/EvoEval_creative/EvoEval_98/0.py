def nature_sequence_generator(n, a, b):
    sequence = [a, b]
    next_natural = 1
    for _ in range(n - 2):
        next_number = sequence[-1] + sequence[-2] + next_natural
        if is_prime(next_number):
            sequence.append('prime')
        else:
            sequence.append(next_number)
        next_natural += 1
    return sequence