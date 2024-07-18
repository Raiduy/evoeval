
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted in descending order.
    """
    third_indices = [l[i] for i in range(len(l)) if i % 3 == 0]
    third_indices.sort(reverse=True)
    sorted_third_indices = []
    for i in range(len(l)):
        if i % 3 == 0:
            sorted_third_indices.append(third_indices.pop(0))
        else:
            sorted_third_indices.append(l[i])
    return sorted_third_indices