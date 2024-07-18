
def list_prime_exchange(lst1, lst2, x, y):
    prime_lst1 = [num for num in lst1 if is_prime(num)]
    non_prime_lst1 = [num for num in lst1 if not is_prime(num)]
    prime_lst2 = [num for num in lst2 if is_prime(num)]
    non_prime_lst2 = [num for num in lst2 if not is_prime(num)]
    if len(non_prime_lst1) == 0:
        return x
    elif len(prime_lst2) == 0:
        return y
    else:
        for num in non_prime_lst1:
            if len(prime_lst2) == 0:
                break
            if num in prime_lst2:
                prime_lst1.append(num)
                prime_lst2.remove(num)
                non_prime_lst1.remove(num)
        if len(non_prime_lst1) == 0:
            return x
        else:
            return y