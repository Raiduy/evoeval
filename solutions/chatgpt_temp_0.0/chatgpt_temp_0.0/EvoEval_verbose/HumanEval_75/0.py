
def is_multiply_prime(a):
    """
    Define a function called 'is_multiply_prime' that takes a single integer input 'a'. The purpose of this function is to determine if the given input number 'a' can be expressed as the multiplication of exactly three prime numbers. If 'a' can be expressed in this way, the function should return a Boolean value of True. If 'a' cannot be expressed as the multiplication of three prime numbers, then the function should return a Boolean value of False.

    The function only works correctly for values of 'a' that are less than 100. If 'a' is 100 or greater, the function's behavior is undefined.

    For example, if the function is called with the input argument of 30 (is_multiply_prime(30)), the function will return True. This is because 30 can be expressed as the multiplication of the three prime numbers 2, 3, and 5 (2*3*5 = 30). However, if the function were called with an input argument of a number that cannot be expressed as the multiplication of three prime numbers, the function would return False.
    """
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for i in primes:
        if a % i == 0:
            quotient = a // i
            for j in primes:
                if quotient % j == 0:
                    remainder = quotient // j
                    for k in primes:
                        if remainder % k == 0:
                            return True
    return False