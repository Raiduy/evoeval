
def largest_prime_odd_ends(nums):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        sqrt_n = int(n ** 0.5) + 1
        for i in range(3, sqrt_n, 2):
            if n % i == 0:
                return False
        return True

    def first_and_last_digit_odd(n):
        first_digit = int(str(n)[0])
        last_digit = int(str(n)[-1])
        return first_digit % 2 == 1 and last_digit % 2 == 1
    largest_prime = None
    for num in nums:
        if num > 10 and first_and_last_digit_odd(num):
            for i in range(num, 2, -1):
                if num % i == 0 and is_prime(i):
                    largest_prime = i
                    break
    return largest_prime