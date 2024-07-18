
def largest_prime_divisor_digit_sum(lst):

    def prime_divisors(n):
        for i in range(n, 0, -1):
            if n % i == 0 and is_prime(i):
                return i
        return 0
    max_divisor = max((prime_divisors(n) for n in lst))
    return sum((int(digit) for digit in str(max_divisor)))