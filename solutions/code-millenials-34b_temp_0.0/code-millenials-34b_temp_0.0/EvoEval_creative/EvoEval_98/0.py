def nature_sequence_generator(n, a, b):

    def is_prime(num):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    return False
            else:
                return True
        else:
            return False
    sequence = [a, b]
    for i in range(2, n):
        next_num = sequence[i - 1] + sequence[i - 2] + 1
        sequence.append(next_num)
    for i in range(n):
        if is_prime(sequence[i]):
            sequence[i] = 'prime'
    return sequence