from typing import List, Any, Union

def filter_and_sort_integers(values):
    integers = [value for value in values if isinstance(value, int)]
    if not integers:
        return 'No integers found'
    for i in range(len(integers) - 1):
        for j in range(len(integers) - 1 - i):
            if integers[j] > integers[j + 1]:
                (integers[j], integers[j + 1]) = (integers[j + 1], integers[j])
    return integers