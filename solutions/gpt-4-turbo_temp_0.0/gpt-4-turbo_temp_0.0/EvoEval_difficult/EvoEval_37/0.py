def sort_even_odd(l: list, m: list):
    even_elements = [l[i] for i in range(0, len(l), 2)]
    sorted_even_elements = []
    for element in m:
        if element in even_elements:
            sorted_even_elements.append(element)
            even_elements.remove(element)
    sorted_even_elements.extend(even_elements)
    result = []
    even_index = 0
    for i in range(len(l)):
        if i % 2 == 0:
            result.append(sorted_even_elements[even_index])
            even_index += 1
        else:
            result.append(l[i])
    return result