def asciiArt(n, s):
    result = ''
    for i in range(n):
        result += '*' + s * n + '*\n'
    result += '*' * (len(s) * n + 2) + '\n'
    return result