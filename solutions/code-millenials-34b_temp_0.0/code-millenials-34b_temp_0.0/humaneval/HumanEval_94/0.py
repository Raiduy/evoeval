

def skjkasdkd(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_values = [i for i in lst if is_prime(i)]
    largest_prime = max(prime_values)
    return sum(int(digit) for digit in str(largest_prime))
