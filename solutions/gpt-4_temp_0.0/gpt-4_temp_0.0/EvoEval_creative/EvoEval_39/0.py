def asciiArt(n, s):
    repeated_s = ''.join([char * n for char in s])
    ascii_art = ['*' + repeated_s + '*'] * n
    ascii_art.append('*' * len(ascii_art[0]))
    ascii_art_str = '\n'.join(ascii_art)
    return ascii_art_str