def asciiArt(n, s):
    art = [['*' for _ in range(len(s) * n + 2)] for _ in range(n + 2)]
    for i in range(1, n + 1):
        for j in range(1, len(s) * n + 1):
            if (j - 1) // n < len(s):
                art[i][j] = s[(j - 1) // n]
    art_str = '\n'.join([''.join(row) for row in art])
    return art_str