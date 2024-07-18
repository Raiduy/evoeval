
def sort_prime_even(l: list, x, y):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted. If the sorted element at an even index
    is prime, replace it with x. Otherwise, replace it with y.

    Examples:
    sort_prime_even([2, 3, 4, 5, 6], 10, 20) == [10, 3, 20, 5, 20]
    sort_prime_even([7, 1, 9, 2, 8], 15, 30) == [15, 1, 30, 2, 30]
    """

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    even_indices = [i for i in range(len(l)) if i % 2 == 0]
    even_values = sorted([l[i] for i in even_indices])
    for (i, val) in zip(even_indices, even_values):
        l[i] = x if is_prime(val) else y
    return l