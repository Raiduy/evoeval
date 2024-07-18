
def modp_count(arr, n: int, p: int):
    """
    Write a function modp_count which takes an array of integers and two integers n and p as inputs.
    The function should first calculate 2^n modulo p. 
    It then counts the number of elements in the array which has a sum of digits > the result of 2^n modulo p.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> modp_count([], 2, 5) == 0
    >>> modp_count([-1, 11, -11], 4, 5) == 1
    >>> modp_count([1, 1, 2], 0, 101) == 1
    >>> modp_count([12, 15, 20], 11, 3) == 2
    """
    mod_result = 2 ** n % p
    count = 0
    for num in arr:
        if num < 0:
            num = -num
        digit_sum = sum((int(digit) for digit in str(num)))
        if digit_sum > mod_result:
            count += 1
    return count