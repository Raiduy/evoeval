
def sort_prime_even(l: list, x, y):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indices, while its values at the even indices are equal
    to the values of the even indices of l, but sorted. If the sorted element at an even index
    is prime, replace it with x. Otherwise, replace it with y.

    Examples:
    sort_prime_even([2, 3, 4, 5, 6], 10, 20) == [10, 3, 20, 5, 20]
    sort_prime_even([7, 1, 9, 2, 8], 15, 30) == [15, 1, 30, 2, 30]
    """
    even_indices_elements = sorted([l[i] for i in range(len(l)) if i % 2 == 0])
    for i in range(len(even_indices_elements)):
        if is_prime(even_indices_elements[i]):
            even_indices_elements[i] = x
        else:
            even_indices_elements[i] = y
    result = []
    even_index = 0
    for i in range(len(l)):
        if i % 2 == 0:
            result.append(even_indices_elements[even_index])
            even_index += 1
        else:
            result.append(l[i])
    return result