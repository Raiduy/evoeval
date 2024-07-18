
def is_multiply_prime(a):
    """
    Define a function called 'is_multiply_prime' that takes a single integer input 'a'. The purpose of this function is to determine if the given input number 'a' can be expressed as the multiplication of exactly three prime numbers. If 'a' can be expressed in this way, the function should return a Boolean value of True. If 'a' cannot be expressed as the multiplication of three prime numbers, then the function should return a Boolean value of False.

    The function only works correctly for values of 'a' that are less than 100. If 'a' is 100 or greater, the function's behavior is undefined.

    For example, if the function is called with the input argument of 30 (is_multiply_prime(30)), the function will return True. This is because 30 can be expressed as the multiplication of the three prime numbers 2, 3, and 5 (2*3*5 = 30). However, if the function were called with an input argument of a number that cannot be expressed as the multiplication of three prime numbers, the function would return False.
    """

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = [i for i in range(2, a) if is_prime(i)]
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            for k in range(j, len(primes)):
                if primes[i] * primes[j] * primes[k] == a:
                    return True
    return False