
def tri(n):
    if n == 0:
        return [3]
    elif n % 2 == 0:
        return [1 + i / 2 for i in range(1, n + 2)]
    else:
        sequence = [1, 3]
        for i in range(2, n + 1):
            sequence.append(sequence[i - 1] + sequence[i - 2] + sequence[i - 3])
        return sequence