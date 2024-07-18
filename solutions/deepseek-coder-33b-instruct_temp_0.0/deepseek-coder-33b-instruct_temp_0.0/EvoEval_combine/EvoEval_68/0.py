
def minOddDigitsProductSubArray(nums):
    min_product = float('inf')
    for i in range(len(nums)):
        product = 1
        for j in range(i, len(nums)):
            for digit in str(nums[j]):
                if int(digit) % 2 != 0:
                    product *= int(digit)
            if product < min_product:
                min_product = product
    return min_product if min_product != float('inf') else 0