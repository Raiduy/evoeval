
def minOddDigitsProductSubArray(nums):
    """
    Given an array of positive integers nums, find the minimum product of odd digits of any 
    non-empty sub-array of nums. For each integer in the sub-array, you need to calculate 
    the product of its odd digits. If all digits are even in an integer, consider its product as 0.
    You need to return the minimum sum of these products.
    
    Example:
    minOddDigitsProductSubArray([2, 3, 4, 1, 2, 4]) == 0
    minOddDigitsProductSubArray([235, 912, 43]) == 3 (as 235 -> 15, 912 -> 9, 43 -> 3)

    Note: 
    A sub-array is a contiguous part of an array. And you should calculate the products for 
    each integer in the sub-array independently.
    """
    min_sum = float('inf')
    for i in range(len(nums)):
        product = 1
        for digit in str(nums[i]):
            if int(digit) % 2 != 0:
                product *= int(digit)
        if product == 1:
            product = 0
        min_sum = min(min_sum, product)
    return min_sum