

def sort_even(l: list):
    even_indices = [i for i in range(0, len(l), 2)]
    even_values = sorted([l[i] for i in even_indices])
    result = []
    for (i, value) in enumerate(l):
        if i in even_indices:
            result.append(even_values.pop(0))
        else:
            result.append(value)
    return result