
import math

def minSubArraySumEvenOdd(nums):

    def countEvenOddDigits(number):
        (even_count, odd_count) = (0, 0)
        number = abs(number)
        if number == 0:
            return (1, 0)
        while number > 0:
            digit = number % 10
            if digit % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
            number //= 10
        return (even_count, odd_count)
    min_sum = math.inf
    current_sum = 0
    for num in nums:
        current_sum = min(num, current_sum + num)
        min_sum = min(min_sum, current_sum)
    return countEvenOddDigits(min_sum)