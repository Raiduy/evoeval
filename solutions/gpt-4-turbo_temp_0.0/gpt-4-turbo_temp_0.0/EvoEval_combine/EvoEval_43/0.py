
def sorted_fib4_sequence(n: int):
    if n == 0:
        return []
    sequence = [0, 0, 2, 0][:n]
    for i in range(4, n):
        next_element = sequence[i - 1] + sequence[i - 2] + sequence[i - 3] + sequence[i - 4]
        sequence.append(next_element)
    if (sequence[0] + sequence[-1]) % 2 == 0:
        sequence.sort(reverse=True)
    else:
        sequence.sort()
    return sequence