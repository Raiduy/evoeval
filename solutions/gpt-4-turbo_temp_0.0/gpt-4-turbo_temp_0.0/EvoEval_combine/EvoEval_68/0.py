
def minOddDigitsProductSubArray(nums):

    def productOfOddDigits(n):
        product = 1
        hasOdd = False
        while n > 0:
            digit = n % 10
            if digit % 2 == 1:
                product *= digit
                hasOdd = True
            n //= 10
        return product if hasOdd else 0
    minProductSum = float('inf')
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            currentProductSum = 0
            for k in range(i, j + 1):
                currentProductSum += productOfOddDigits(nums[k])
            minProductSum = min(minProductSum, currentProductSum)
    return minProductSum if minProductSum != float('inf') else 0