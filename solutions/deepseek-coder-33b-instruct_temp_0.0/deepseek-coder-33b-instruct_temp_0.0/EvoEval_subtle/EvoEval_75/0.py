
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 4 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(90) == True
    90 = 2 * 3 * 3 * 5
    """

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = [i for i in range(2, a) if is_prime(i)]
    for i in primes:
        for j in primes:
            for k in primes:
                for l in primes:
                    if i * j * k * l == a:
                        return True
    return False