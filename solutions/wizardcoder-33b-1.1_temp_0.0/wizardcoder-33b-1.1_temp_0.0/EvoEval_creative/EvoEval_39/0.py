def asciiArt(n, s):
    top_bottom = '*' + s * n + '*'
    middle = '\n*' + s * n + '*\n'
    ascii_art = top_bottom + middle * n + top_bottom
    return ascii_art