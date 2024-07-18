
def minOddDigitsProductSubArray(nums):
    n = len(nums)
    min_product = float('inf')
    for i in range(n):
        product = 1
        for j in range(i, n):
            odd_digits_product = 1
            for num in nums[i:j + 1]:
                odd_digits = [int(d) for d in str(num) if int(d) % 2 != 0]
                if odd_digits:
                    odd_digits_product *= int(''.join(map(str, odd_digits)))
            product *= odd_digits_product
            min_product = min(min_product, product)
    return min_product