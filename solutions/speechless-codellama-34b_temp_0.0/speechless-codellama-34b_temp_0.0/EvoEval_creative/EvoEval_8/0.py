def transform_canvas(canvas: str) -> str:
    if canvas.count('P') > 1 or canvas.count('-') % canvas.count('P') == 0:
        return 'Invalid canvas'
    if 'P' not in canvas:
        return canvas
    start_index = canvas.index('P')
    painted = set()
    for i in range(start_index, len(canvas)):
        if canvas[i] == '-':
            painted.add(i)
            if i + 1 < len(canvas) and canvas[i + 1] != '#':
                painted.add(i + 1)
            if i - 1 >= 0 and canvas[i - 1] != '#':
                painted.add(i - 1)
    for i in painted:
        canvas = canvas[:i] + '*' + canvas[i + 1:]
    return canvas