
def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than or equal to n. Return the list in descending order.
    for example:
    count_up_to(5) => [5,3,2]
    count_up_to(11) => [11,7,5,3,2]
    count_up_to(0) => []
    count_up_to(20) => [19,17,13,11,7,5,3,2]
    count_up_to(1) => []
    count_up_to(18) => [17,13,11,7,5,3,2]
    """

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    primes = [i for i in range(2, n + 1) if is_prime(i)]
    return sorted(primes, reverse=True)