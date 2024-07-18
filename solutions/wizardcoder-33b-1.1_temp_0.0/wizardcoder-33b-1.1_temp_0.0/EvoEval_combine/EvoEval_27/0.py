
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
    for num in lst1:
        if not is_prime(num):
            return y
    for num in lst2:
        if is_prime(num):
            return y
    return x