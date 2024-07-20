def is_prime(n):
    """
    This function, is_prime, takes an integer as input, with the name 'n'. The purpose of this function is to check if 'n' is a prime number or not. 
    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. If 'n' is prime, the function will return 
    True, and if 'n' is not prime (i.e., it has other divisors besides 1 and itself), the function will return False.
    
    The function works by iterating through all numbers from 2 up to 'n' and checking if 'n' is divisible by any of these numbers. If 'n' is divisible by 
    any number other than 1 and itself, it is not a prime number, and the function will return False. If 'n' is not divisible by any number other than 1 
    and itself, it is a prime number, and the function will return True.

    Examples:
    >>> is_prime(6)
    False
    This is because 6 is divisible by 2 and 3, in addition to 1 and itself.

    >>> is_prime(101)
    True
    This is because 101 is only divisible by 1 and itself.

    >>> is_prime(11)
    True
    This is because 11 is only divisible by 1 and itself.

    >>> is_prime(13441)
    True
    This is because 13441 is only divisible by 1 and itself.

    >>> is_prime(61)
    True
    This is because 61 is only divisible by 1 and itself.

    >>> is_prime(4)
    False
    This is because 4 is divisible by 2, in addition to 1 and itself.

    >>> is_prime(1)
    False
    This is because 1 is not considered a prime number.
    """
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True