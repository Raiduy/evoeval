
def count_nums(arr):

    def sum_of_digits(n):
        """
        Helper function to calculate the sum of digits of a number.
        Takes into account the sign of the number.
        """
        if n < 0:
            return -sum(map(int, str(-n)))
        else:
            return sum(map(int, str(n)))
    count = 0
    for num in arr:
        if sum_of_digits(num) > 0:
            count += 1
    return count