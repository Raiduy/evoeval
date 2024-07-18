def complexity_increased(lst, n):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    if not any((x > 0 for x in lst)):
        return -1
    prime_numbers = [x for x in lst if is_prime(x)]
    if not prime_numbers:
        return -1
    return sum((sum((int(digit) ** n for digit in str(num))) for num in prime_numbers))