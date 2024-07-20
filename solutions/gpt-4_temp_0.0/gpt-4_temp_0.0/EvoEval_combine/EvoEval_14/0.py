
def prime_avg_range(n, m):
    """You are given two positive integers n and m. Your task is to create a list of all 
    prime numbers between n and m (inclusive), compute the average of these prime numbers, 
    round the answer to the nearest integer, and convert that to binary. 
    If there are no prime numbers in the range or if n is greater than m, return -1.
    Example:
    prime_avg_range(1, 5) => "0b11"
    prime_avg_range(7, 11) => "0b1001"
    prime_avg_range(20, 30) => "0b11010"
    prime_avg_range(15, 10) => -1
    prime_avg_range(10, 10) => -1
    """
    if n > m:
        return -1

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    primes = [i for i in range(n, m + 1) if is_prime(i)]
    if not primes:
        return -1
    avg = round(sum(primes) / len(primes))
    return bin(avg)