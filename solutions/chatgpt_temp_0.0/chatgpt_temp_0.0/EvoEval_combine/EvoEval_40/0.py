
def largest_prime_odd_ends(nums):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def get_first_digit(n):
        return int(str(n)[0])

    def get_last_digit(n):
        return int(str(n)[-1])
    prime_factors = []
    for num in nums:
        if num > 10 and get_first_digit(num) % 2 != 0 and (get_last_digit(num) % 2 != 0):
            for i in range(2, num + 1):
                if num % i == 0 and is_prime(i):
                    prime_factors.append(i)
    if prime_factors:
        return max(prime_factors)
    else:
        return None