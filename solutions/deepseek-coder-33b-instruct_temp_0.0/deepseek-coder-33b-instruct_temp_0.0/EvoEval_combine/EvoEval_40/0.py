
def largest_prime_odd_ends(nums):

    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2):
            return False
        return all((n % i for i in range(3, int(n ** 0.5) + 1, 2)))

    def is_odd_ends(n):
        n = abs(n)
        return int(str(n)[0]) % 2 == 1 and int(str(n)[-1]) % 2 == 1
    primes = [num for num in nums if num > 10 and is_odd_ends(num) and is_prime(num)]
    return max(primes) if primes else None