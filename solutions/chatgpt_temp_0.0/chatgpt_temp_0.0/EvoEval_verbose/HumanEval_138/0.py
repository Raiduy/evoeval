
def is_equal_to_sum_even(n):
    if n % 8 == 0:
        return True
    elif n >= 16 and (n - 8) % 8 == 0:
        return True
    elif n >= 24 and (n - 16) % 8 == 0:
        return True
    elif n >= 32 and (n - 24) % 8 == 0:
        return True
    else:
        return False