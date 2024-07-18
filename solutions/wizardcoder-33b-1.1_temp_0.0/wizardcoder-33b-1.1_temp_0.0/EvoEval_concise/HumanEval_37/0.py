

def sort_even(l: list):
    even_indexed_elements = sorted((l[i] for i in range(0, len(l), 2)))
    result = []
    for i in range(len(l)):
        if i % 2 == 0:
            result.append(even_indexed_elements.pop(0))
        else:
            result.append(l[i])
    return result