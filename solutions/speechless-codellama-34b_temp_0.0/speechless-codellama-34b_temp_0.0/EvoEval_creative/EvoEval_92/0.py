def paint_fountain(n):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    layers = []
    for i in range(n):
        layer = ''
        width = 2 * i + 1
        for j in range(width):
            if j == width // 2:
                layer += 'A'
            else:
                layer += alphabet[(i + j) % 26]
        layers.append(layer.center(width))
    return '\n'.join(layers)