

def skjkasdkd(lst):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime_numbers = [i for i in lst if is_prime(i)]
    if not prime_numbers:
        return 0
    largest_prime = max(prime_numbers)
    return sum((int(digit) for digit in str(largest_prime)))