def incr_list_conditionally(l: list, ignore: list):
    if any((not isinstance(i, int) for i in ignore)):
        return 'Ignore list should only contain integers'
    return [i + 1 if i not in ignore else i for i in l]