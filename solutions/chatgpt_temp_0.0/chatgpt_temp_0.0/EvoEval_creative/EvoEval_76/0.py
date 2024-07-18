def create_pyramid(lst):
    pyramid = []
    for num in reversed(lst):
        level = '#' * num
        pyramid.insert(0, level)
    return pyramid