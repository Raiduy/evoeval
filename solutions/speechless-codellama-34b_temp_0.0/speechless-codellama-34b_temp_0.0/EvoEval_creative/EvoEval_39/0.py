def asciiArt(n, s):
    s_len = len(s)
    rows = []
    rows.append('*' + s * n + '*')
    for i in range(s_len):
        row = '*'
        for j in range(s_len):
            if i == 0 or i == s_len - 1 or j == 0 or (j == s_len - 1):
                row += '*'
            else:
                row += s[j] * n
        rows.append(row)
    rows.append('*' + s * n + '*')
    return '\n'.join(rows)