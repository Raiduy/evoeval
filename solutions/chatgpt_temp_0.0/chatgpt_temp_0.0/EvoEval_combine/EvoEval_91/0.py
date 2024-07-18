
def sort_prime_even(l: list, x, y):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted. If the sorted element at an even index
    is prime, replace it with x. Otherwise, replace it with y.

    Examples:
    sort_prime_even([2, 3, 4, 5, 6], 10, 20) == [10, 3, 20, 5, 20]
    sort_prime_even([7, 1, 9, 2, 8], 15, 30) == [15, 1, 30, 2, 30]
    """
    even_indices = [l[i] for i in range(len(l)) if i % 2 == 0]
    sorted_even_indices = sorted(even_indices)
    prime_indices = [x if num in sorted_even_indices and is_prime(num) else y for num in l]
    return [prime_indices[i] if i % 2 == 0 else l[i] for i in range(len(l))]