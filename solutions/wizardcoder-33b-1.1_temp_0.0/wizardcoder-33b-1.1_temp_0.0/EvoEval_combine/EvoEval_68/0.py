
def minOddDigitsProductSubArray(nums):
    min_product = float('inf')
    for i in range(len(nums)):
        product = 1
        for digit in str(nums[i]):
            if int(digit) % 2 != 0:
                product *= int(digit)
        if product != 1:
            min_product = min(min_product, product)
    return min_product if min_product != float('inf') else 0