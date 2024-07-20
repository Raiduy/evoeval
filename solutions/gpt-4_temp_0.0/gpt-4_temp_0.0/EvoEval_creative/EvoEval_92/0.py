def paint_fountain(n):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    fountain = []
    for i in range(n):
        layer = [' '] * (2 * n - 1)
        for j in range(i + 1):
            layer[n - 1 - j] = layer[n - 1 + j] = alphabet[j % 26]
        fountain.append(''.join(layer))
    return '\n'.join(fountain)