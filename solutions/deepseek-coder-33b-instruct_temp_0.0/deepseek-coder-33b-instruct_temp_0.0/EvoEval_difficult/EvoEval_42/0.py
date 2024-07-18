def incr_list_conditionally(l: list, ignore: list):
    if not all((isinstance(i, int) for i in ignore)):
        raise ValueError('Ignore list should only contain integers')
    return [i + 1 if i not in ignore else i for i in l]