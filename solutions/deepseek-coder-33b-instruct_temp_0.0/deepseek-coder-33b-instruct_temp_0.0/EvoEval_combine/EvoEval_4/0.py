
def largest_prime_divisor_digit_sum(lst: list) -> int:

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

    def largest_prime_divisor(n):
        largest = 2
        for i in range(2, n):
            if n % i == 0 and is_prime(i):
                largest = i
        return largest

    def digit_sum(n):
        return sum((int(digit) for digit in str(n)))
    largest_prime_divisors = [largest_prime_divisor(n) for n in lst]
    return max((digit_sum(n) for n in largest_prime_divisors))