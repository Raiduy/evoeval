

def sort_third(l: list):
    sorted_elements = sorted((element for (index, element) in enumerate(l) if index % 3 == 0))
    return [sorted_elements.pop(0) if index % 3 == 0 else element for (index, element) in enumerate(l)]