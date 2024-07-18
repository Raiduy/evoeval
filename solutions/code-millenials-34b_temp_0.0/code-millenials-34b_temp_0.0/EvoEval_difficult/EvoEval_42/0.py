def incr_list_conditionally(l: list, ignore: list):
    try:
        new_list = [num + 1 if num not in ignore else num for num in l]
        return new_list
    except TypeError:
        return 'Ignore list should only contain integers'