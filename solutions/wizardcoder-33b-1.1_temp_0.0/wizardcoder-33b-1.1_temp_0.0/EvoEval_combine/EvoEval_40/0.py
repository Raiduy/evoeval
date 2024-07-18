
def largest_prime_odd_ends(nums):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_odd_ends(n):
        n = abs(n)
        return int(str(n)[0]) % 2 != 0 and int(str(n)[-1]) % 2 != 0
    primes = [num for num in nums if num > 10 and is_prime(num) and is_odd_ends(num)]
    return max(primes) if primes else None