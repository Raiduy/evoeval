
def largest_prime_odd_ends(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    largest_prime = None
    for num in nums:
        if num > 10 and num % 10 % 2 == 1 and (num // 10 % 2 == 1):
            for factor in range(3, int(num ** 0.5) + 1, 2):
                if num % factor == 0 and is_prime(factor):
                    largest_prime = max(largest_prime, factor)
    return largest_prime