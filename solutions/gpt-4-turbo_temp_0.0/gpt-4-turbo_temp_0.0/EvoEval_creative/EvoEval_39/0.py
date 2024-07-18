def asciiArt(n, s):
    repeated_pattern = ''.join([char * n for char in s])
    top_and_middle = '\n'.join(['*' + repeated_pattern + '*' for _ in range(n)])
    bottom = '*' * (len(repeated_pattern) + 2)
    ascii_art = top_and_middle + '\n' + bottom
    return ascii_art