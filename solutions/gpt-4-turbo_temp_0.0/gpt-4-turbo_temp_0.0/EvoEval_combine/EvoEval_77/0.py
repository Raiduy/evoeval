
def mixed_solution(arr):

    def sum_of_digits(n):
        """
        Helper function to calculate the sum of digits of a number.
        Takes into account the sign of the first digit for negative numbers.
        """
        if n < 0:
            return -int(str(n)[1]) + sum((int(digit) for digit in str(n)[2:]))
        else:
            return sum((int(digit) for digit in str(n)))
    total = 0
    for i in range(0, len(arr), 2):
        if arr[i] % 2 != 0 and sum_of_digits(arr[i]) > 0:
            total += arr[i]
    return total