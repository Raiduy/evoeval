def incr_list_conditionally(l: list, ignore: list):
    for num in ignore:
        if not isinstance(num, int):
            return 'Ignore list should only contain integers'
    result = []
    for element in l:
        if element not in ignore:
            result.append(element + 1)
        else:
            result.append(element)
    return result