
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indices that are not divisible by three, while its values at the indices that are divisible by three are equal
    to the values of the corresponding indices of l, but sorted in descending order.
    """
    divisible_by_three_elements = [l[i] for i in range(len(l)) if (i + 1) % 3 == 0]
    divisible_by_three_elements_sorted = sorted(divisible_by_three_elements, reverse=True)
    result = []
    sort_index = 0
    for i in range(len(l)):
        if (i + 1) % 3 == 0:
            result.append(divisible_by_three_elements_sorted[sort_index])
            sort_index += 1
        else:
            result.append(l[i])
    return result