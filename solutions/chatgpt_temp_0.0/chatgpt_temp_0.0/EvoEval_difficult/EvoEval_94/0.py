def complexity_increased(lst, n):
    if not any((x > 0 for x in lst)):
        return -1

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def sum_of_digits(num, power):
        return sum((int(digit) ** power for digit in str(num)))
    prime_sum = 0
    for num in lst:
        if is_prime(num):
            prime_sum += sum_of_digits(num, n)
    if prime_sum == 0:
        return -1
    else:
        return prime_sum