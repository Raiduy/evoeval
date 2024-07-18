def nature_sequence_generator(n, a, b):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    sequence = [a, b]
    for i in range(2, n):
        next_num = sequence[i - 1] + sequence[i - 2] + i
        sequence.append(next_num)
    for i in range(len(sequence)):
        if is_prime(sequence[i]):
            sequence[i] = 'prime'
    return sequence