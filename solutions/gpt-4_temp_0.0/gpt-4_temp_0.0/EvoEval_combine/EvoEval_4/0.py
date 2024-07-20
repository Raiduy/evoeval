
def largest_prime_divisor_digit_sum(lst):
    largest_prime = 0
    for num in lst:
        if is_prime(num):
            largest_prime = max(largest_prime, num)
        else:
            for i in range(num - 1, 1, -1):
                if num % i == 0 and is_prime(i):
                    largest_prime = max(largest_prime, i)
                    break
    return sum((int(digit) for digit in str(largest_prime)))