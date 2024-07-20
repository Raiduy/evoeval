
def sort_prime_even(l: list, x, y):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    even_indices = [l[i] for i in range(len(l)) if i % 2 == 0]
    even_indices.sort()
    for i in range(len(l)):
        if i % 2 == 0:
            if is_prime(even_indices[0]):
                l[i] = x
            else:
                l[i] = y
            even_indices.pop(0)
    return l