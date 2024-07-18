
def get_odd_collatz(n):
    if n < 1:
        raise ValueError('Input must be a positive integer')
    if n == 1:
        return [1]
    collatz_sequence = []
    while n != 1:
        collatz_sequence.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    collatz_sequence.append(1)
    odd_collatz_sequence = [num for num in collatz_sequence if num % 2 != 0]
    return sorted(odd_collatz_sequence)