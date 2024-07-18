def paint_fountain(n):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    fountain = []
    for i in range(n):
        letter = alphabet[i % 26]
        width = 2 * i + 1
        layer = letter * width
        layer = layer.center(2 * n - 1, ' ')
        fountain.append(layer)
    return '\n'.join(fountain)