from typing import List, Any, Union

def filter_and_sort_integers(values: List[Any]) -> Union[List[int], str]:
    integers = [i for i in values if isinstance(i, int)]
    if not integers:
        return 'No integers found'
    for i in range(len(integers)):
        for j in range(len(integers) - 1):
            if integers[j] > integers[j + 1]:
                (integers[j], integers[j + 1]) = (integers[j + 1], integers[j])
    return integers