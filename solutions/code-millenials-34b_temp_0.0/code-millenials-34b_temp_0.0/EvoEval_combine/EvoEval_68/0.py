
def minOddDigitsProductSubArray(nums):

    def oddDigitsProduct(n):
        product = 1
        for digit in str(n):
            if int(digit) % 2 != 0:
                product *= int(digit)
        return product if product != 1 else 0
    minProduct = float('inf')
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            subArray = nums[i:j + 1]
            productSum = sum((oddDigitsProduct(n) for n in subArray))
            minProduct = min(minProduct, productSum)
    return minProduct