
def mixed_solution(arr):

    def sum_digits(n):
        return sum((int(digit) for digit in str(abs(n))))
    return sum((num for (i, num) in enumerate(arr) if i % 2 == 0 and num % 2 != 0 and (sum_digits(num) > 0)))