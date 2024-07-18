def create_pyramid(lst):
    if not lst:
        return []
    pyramid = []
    for i in range(len(lst)):
        level = ''.join(['#' for _ in range(sum(lst[:i + 1]))])
        pyramid.append(level)
    return pyramid