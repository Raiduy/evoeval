def word_spiral(arr):
    if not arr:
        return ''
    result = ''
    row_start = 0
    row_end = len(arr) - 1
    col_start = 0
    col_end = len(arr[0]) - 1
    while row_start <= row_end and col_start <= col_end:
        for i in range(col_start, col_end + 1):
            result += arr[row_start][i]
        row_start += 1
        for i in range(row_start, row_end + 1):
            result += arr[i][col_end]
        col_end -= 1
        if row_start <= row_end:
            for i in range(col_end, col_start - 1, -1):
                result += arr[row_end][i]
            row_end -= 1
        if col_start <= col_end:
            for i in range(row_end, row_start - 1, -1):
                result += arr[i][col_start]
            col_start += 1
    return result