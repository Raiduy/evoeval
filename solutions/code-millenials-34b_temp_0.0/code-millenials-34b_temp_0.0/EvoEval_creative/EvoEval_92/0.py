def paint_fountain(n):
    alphabet = [chr(i) for i in range(65, 91)]
    layers = []
    for i in range(n):
        layer = ''
        width = 2 * min(i, n - 1 - i) + 1
        offset = abs(i - n + 1)
        for j in range(width):
            if j < offset or j >= width - offset:
                layer += ' '
            else:
                layer += alphabet[(i + j - offset) % 26]
        layers.append(layer.center(2 * n - 1))
    return '\n'.join(layers)