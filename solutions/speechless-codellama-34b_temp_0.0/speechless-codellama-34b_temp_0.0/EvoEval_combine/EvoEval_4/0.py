
def largest_prime_divisor_digit_sum(lst: list) -> int:

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    largest_prime = 0
    for num in lst:
        if is_prime(num):
            largest_prime = max(largest_prime, num)
        else:
            for i in range(2, num):
                if num % i == 0 and is_prime(i):
                    largest_prime = max(largest_prime, i)
    return sum((int(digit) for digit in str(largest_prime)))