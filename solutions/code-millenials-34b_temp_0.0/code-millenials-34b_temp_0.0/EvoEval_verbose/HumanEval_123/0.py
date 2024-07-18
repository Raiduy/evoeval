
def get_odd_collatz(n):

    def collatz(n):
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
        return [1]
    collatz_sequence = collatz(n)
    odd_numbers = [i for i in collatz_sequence if i % 2 != 0]
    return sorted(odd_numbers)