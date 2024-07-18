def paint_fountain(n):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    layers = []
    for i in range(n):
        layer = alphabet[i] * (2 * i + 1)
        layer = layer.center(2 * n - 1)
        layers.append(layer)
    return '\n'.join(layers)