
def largest_prime_divisor_digit_sum(lst: list) -> int:
    """Find the largest prime divisor (or the number itself if prime) with the largest digit sum."""
    largest_prime = 0
    for number in lst:
        prime_divisor = largest_prime_divisor(number)
        if prime_divisor > largest_prime:
            largest_prime = prime_divisor
    return digit_sum(largest_prime)