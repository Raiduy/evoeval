
def get_odd_collatz(n):
    def collatz(n):
        sequence = []
        while n != 1:
            sequence.append(n)
            n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(1)
        return sequence

    collatz_sequence = collatz(n)
    odd_numbers = [num for num in collatz_sequence if num % 2 != 0]
    return sorted(odd_numbers)
