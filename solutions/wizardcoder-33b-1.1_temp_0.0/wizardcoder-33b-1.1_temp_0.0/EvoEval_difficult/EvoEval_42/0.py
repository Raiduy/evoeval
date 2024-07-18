def incr_list_conditionally(l: list, ignore: list):
    if all((isinstance(i, int) for i in ignore)):
        return [i + 1 if i not in ignore else i for i in l]
    else:
        return 'Ignore list should only contain integers'