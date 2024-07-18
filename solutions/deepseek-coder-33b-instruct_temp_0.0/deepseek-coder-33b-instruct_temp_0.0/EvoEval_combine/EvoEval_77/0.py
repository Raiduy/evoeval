
def mixed_solution(arr):

    def sum_of_digits(n):
        return sum((int(digit) for digit in str(abs(n))))
    return sum((n for (i, n) in enumerate(arr) if i % 2 == 0 and n % 2 != 0 and (sum_of_digits(n) > 0)))