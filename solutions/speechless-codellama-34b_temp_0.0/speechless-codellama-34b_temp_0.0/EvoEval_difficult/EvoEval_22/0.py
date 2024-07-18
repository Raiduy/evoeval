from typing import List, Any, Union

def filter_and_sort_integers(values: List[Any]) -> Union[List[int], str]:
    integers = []
    for value in values:
        if isinstance(value, int):
            integers.append(value)
    if not integers:
        return 'No integers found'
    for i in range(len(integers)):
        for j in range(i + 1, len(integers)):
            if integers[i] > integers[j]:
                (integers[i], integers[j]) = (integers[j], integers[i])
    return integers