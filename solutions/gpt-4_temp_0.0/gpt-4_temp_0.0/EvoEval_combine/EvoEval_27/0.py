
def list_prime_exchange(lst1, lst2, x, y):
    """The function takes two lists of numbers lst1 and lst2, and two integers x and y. The task is to 
    determine whether it is possible to perform an exchange of elements between lst1 and lst2 to 
    make lst1 a list of only prime numbers. 

    If it is possible, return the value of x. If it is not possible, return the value of y. 

    There is no limit on the number of exchanged elements between lst1 and lst2.

    For example:
    list_prime_exchange([1, 2, 3, 4], [5, 7, 11, 13], 10, 20) => 10
    list_prime_exchange([1, 2, 3, 4], [6, 8, 10, 12], 30, 40) => 40

    It is assumed that the input lists will be non-empty and the integers x and y will be non-zero.
    """

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    non_primes_in_lst1 = sum((not is_prime(i) for i in lst1))
    primes_in_lst2 = sum((is_prime(i) for i in lst2))
    if non_primes_in_lst1 <= primes_in_lst2:
        return x
    else:
        return y