def create_pyramid(p):
    blocks_in_layers = [p]
    while True:
        if p % 2 == 0:
            p -= 2
        else:
            p -= 3
        if p <= 0:
            break
        blocks_in_layers.append(p)
    return blocks_in_layers