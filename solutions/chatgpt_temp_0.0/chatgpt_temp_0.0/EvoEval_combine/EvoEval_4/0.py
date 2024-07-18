
def largest_prime_divisor_digit_sum(lst: list) -> int:

    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def digit_sum(n: int) -> int:
        return sum((int(digit) for digit in str(n)))
    largest_prime_divisor_sum = 0
    for num in lst:
        largest_prime_divisor = 0
        for i in range(2, num):
            if num % i == 0 and is_prime(i):
                largest_prime_divisor = max(largest_prime_divisor, i)
        if largest_prime_divisor == 0:
            largest_prime_divisor_sum += digit_sum(num)
        else:
            largest_prime_divisor_sum += digit_sum(largest_prime_divisor)
    return largest_prime_divisor_sum