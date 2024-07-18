
def list_prime_exchange(lst1, lst2, x, y):
    prime_lst1 = [num for num in lst1 if is_prime(num)]
    not_prime_lst1 = [num for num in lst1 if not is_prime(num)]
    prime_lst2 = [num for num in lst2 if is_prime(num)]
    not_prime_lst2 = [num for num in lst2 if not is_prime(num)]
    if len(prime_lst1) + len(prime_lst2) >= len(lst1):
        return x
    else:
        return y