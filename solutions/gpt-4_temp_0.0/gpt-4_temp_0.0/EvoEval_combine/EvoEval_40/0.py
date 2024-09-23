
def largest_prime_odd_ends(nums):
    """Write a function that takes an array of numbers as input and returns 
    the largest prime factor of the elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9). 
    Assume all numbers in the array are integers and are greater than 1.
    If no prime factor satisfies the condition, return None.
    For example:
    largest_prime_odd_ends([15, -73, 14, -15]) => 5 
    largest_prime_odd_ends([33, -2, -3, 45, 21, 109]) => 109
    largest_prime_odd_ends([10, -2, -3, 5, 21, 4]) => None
    """

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def odd_ends(n):
        str_n = str(n)
        return str_n[0] in '13579' and str_n[-1] in '13579'
    prime_factors = []
    for num in nums:
        if num > 10 and odd_ends(num) and is_prime(num):
            prime_factors.append(num)
    return max(prime_factors) if prime_factors else None