def create_pyramid(p):
    layers = [p]
    while p > 0:
        if p % 2 == 0:
            p -= 2
        else:
            p -= 3
        layers.append(p)
    return layers[::-1]