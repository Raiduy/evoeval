def largest_prime_factor(n: int, m: int):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    if is_prime(m):
        largest = 0
        for i in range(2, n + 1):
            if n % i == 0 and is_prime(i) and (i > largest):
                largest = i
        return largest
    else:
        smallest = n
        for i in range(2, n + 1):
            if n % i == 0 and is_prime(i) and (i < smallest):
                smallest = i
        return smallest