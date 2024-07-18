def order_by_points(nums):

    def sum_of_digits(n):
        return sum((int(digit) for digit in str(abs(n))))
    nums.sort(key=sum_of_digits)
    return nums