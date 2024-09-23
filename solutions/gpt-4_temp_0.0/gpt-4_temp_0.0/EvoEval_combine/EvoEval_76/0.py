def sort_prime_digit_sum(lst):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def digit_sum(n):
        return sum((int(digit) for digit in str(n)))
    new_lst = [digit_sum(n) if is_prime(n) else n for n in lst]
    if (new_lst[0] + new_lst[-1]) % 2 == 0:
        return sorted(new_lst, reverse=True)
    else:
        return sorted(new_lst)