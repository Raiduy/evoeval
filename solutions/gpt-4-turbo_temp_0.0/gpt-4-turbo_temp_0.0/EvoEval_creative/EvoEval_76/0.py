def create_pyramid(lst):
    pyramid = []
    for num in reversed(lst):
        level = '#' * num
        pyramid.append(level)
    return pyramid[::-1]