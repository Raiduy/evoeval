def create_pyramid(lst):
    if not lst:
        return []
    pyramid = []
    current_level = lst[0]
    while current_level > 0:
        level_string = '#' * current_level
        pyramid.append(level_string)
        current_level -= lst.pop(0)
    return pyramid