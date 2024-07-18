
def is_multiply_prime(a):
    """Returns true if the given number is the multiplication of 3 prime numbers and false otherwise."""
    if a < 2:
        return False
    
    primes = [i for i in range(2, a) if is_prime(i)]
    
    # Check combinations of three prime numbers
    for i in range(len(primes)):
        for j in range(i+1, len(primes)):
            for k in range(j+1, len(primes)):
                if primes[i] * primes[j] * primes[k] == a:
                    return True
    return False
