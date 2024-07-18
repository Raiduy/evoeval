
def sorted_fib4_sequence(n: int):
    sequence = [0, 0, 2, 0]
    if n <= 3:
        return sequence[:n]
    for i in range(4, n + 1):
        sequence.append(sequence[i - 1] + sequence[i - 2] + sequence[i - 3] + sequence[i - 4])
    if (sequence[0] + sequence[-1]) % 2 == 0:
        return sorted(sequence, reverse=True)
    else:
        return sorted(sequence)