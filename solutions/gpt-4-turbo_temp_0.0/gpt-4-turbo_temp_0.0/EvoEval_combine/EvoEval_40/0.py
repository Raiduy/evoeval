
def largest_prime_odd_ends(nums):

    def has_odd_ends(n):
        """Check if a number has both first and last digits odd."""
        str_n = str(abs(n))
        return str_n[0] in '13579' and str_n[-1] in '13579'

    def largest_prime_factor(n):
        """Find the largest prime factor of a number."""
        largest_prime = None
        while n % 2 == 0:
            largest_prime = 2
            n //= 2
        for i in range(3, int(n ** 0.5) + 1, 2):
            while n % i == 0:
                largest_prime = i
                n //= i
        if n > 2:
            largest_prime = n
        return largest_prime
    prime_factors = [largest_prime_factor(num) for num in nums if num > 10 and has_odd_ends(num)]
    return max(prime_factors) if prime_factors else None