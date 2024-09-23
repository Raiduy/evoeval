
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

    def product_of_odd_digits(n):
        product = 1
        has_odd = False
        while n:
            (n, digit) = divmod(n, 10)
            if digit % 2 == 1:
                product *= digit
                has_odd = True
        return product if has_odd else 0
    min_product = float('inf')
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            product_sum = sum((product_of_odd_digits(n) for n in nums[i:j + 1]))
            min_product = min(min_product, product_sum)
    return min_product