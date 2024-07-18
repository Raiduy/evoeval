def create_pyramid(p):
    pyramid = []
    while p > 0:
        pyramid.append(p)
        if p % 2 == 0:
            p -= 2
        else:
            p -= 3
    return pyramid[::-1]