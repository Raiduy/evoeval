
def list_prime_exchange(lst1, lst2, x, y):
    for num in lst1:
        if not is_prime(num):
            if num in lst2:
                lst2.remove(num)
            else:
                return y
    return x