
def is_multiply_prime(a):
    count = 0
    for i in range(2, a):
        if a % i == 0 and is_prime(i):
            count += 1
    return count == 3