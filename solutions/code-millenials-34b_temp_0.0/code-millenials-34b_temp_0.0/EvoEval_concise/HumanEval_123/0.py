
def get_odd_collatz(n):
    collatz_sequence = []
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        collatz_sequence.append(n)
    odd_collatz = list(set(collatz_sequence))
    odd_collatz = [i for i in odd_collatz if i % 2 != 0]
    odd_collatz.sort()
    return odd_collatz