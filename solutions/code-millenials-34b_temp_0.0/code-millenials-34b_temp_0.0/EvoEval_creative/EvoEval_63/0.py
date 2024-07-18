def create_pyramid(p):
    pyramid = [p]
    while p > 2:
        if p % 2 == 0:
            p -= 2
        else:
            p -= 3
        pyramid.append(p)
    return pyramid