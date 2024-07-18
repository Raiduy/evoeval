

def sort_third(l: list):
    # Create a list of elements at indices divisible by 3
    divisible_by_3 = sorted([l[i] for i in range(len(l)) if i % 3 == 0])

    # Create a new list with elements at indices divisible by 3 replaced by sorted elements
    new_list = [divisible_by_3.pop(0) if i % 3 == 0 else l[i] for i in range(len(l))]

    return new_list
