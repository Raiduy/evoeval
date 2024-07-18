def paint_fountain(n):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    fountain_layers = []
    for layer in range(n):
        letter = alphabet[layer % 26]
        layer_str = (letter * (layer * 2 + 1)).center(2 * n - 1)
        layer_str = layer_str[:n - 1] + 'A' + layer_str[n:]
        fountain_layers.append(layer_str)
    return '\n'.join(fountain_layers)