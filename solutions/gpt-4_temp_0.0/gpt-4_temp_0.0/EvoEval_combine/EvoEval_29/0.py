def largest_prime_factor_or_value(n, x, y):

    def is_prime(num):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    return False
            else:
                return True
        else:
            return False

    def largest_prime_factor(num):
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            else:
                num //= i
        return num
    if n == 1:
        return y
    elif is_prime(n):
        return x
    else:
        return largest_prime_factor(n)