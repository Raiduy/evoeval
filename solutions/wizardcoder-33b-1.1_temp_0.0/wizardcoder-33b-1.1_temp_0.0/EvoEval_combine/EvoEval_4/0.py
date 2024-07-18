
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
        for i in range(n - 1, 0, -1):
            if n % i == 0 and is_prime(i):
                return i
        return n

    def digit_sum(n):
        return sum((int(digit) for digit in str(n)))
    return max((digit_sum(largest_prime_divisor(n)) for n in lst))