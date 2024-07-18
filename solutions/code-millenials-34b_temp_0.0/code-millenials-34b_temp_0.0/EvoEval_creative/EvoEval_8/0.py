def transform_canvas(canvas: str) -> str:
    start_index = canvas.find('P')
    if start_index == -1:
        return canvas
    if canvas.count('P') > 1 or canvas.count('-') % 2 == 1:
        return 'Invalid canvas'
    new_canvas = list(canvas)
    for i in range(start_index, len(canvas)):
        if new_canvas[i] == '-':
            new_canvas[i] = '*'
        else:
            break
    return ''.join(new_canvas)