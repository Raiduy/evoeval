def asciiArt(n, s):
    top_bottom_row = '*' + '*'.join((n * s for s in s)) + '*'
    middle_rows = ['*' + '*'.join((n * s for s in s)) + '*' for _ in range(n)]
    rows = [top_bottom_row] + middle_rows + [top_bottom_row]
    return '\n'.join(rows)