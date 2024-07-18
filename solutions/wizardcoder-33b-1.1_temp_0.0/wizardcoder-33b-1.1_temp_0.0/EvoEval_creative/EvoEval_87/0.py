def word_spiral(arr):
    if not arr:
        return ''
    result = []
    while arr:
        result.extend(arr.pop(0))
        if not arr:
            break
        for row in arr:
            result.append(row.pop())
        result.extend(arr.pop()[::-1])
        if not arr:
            break
        for row in arr[::-1]:
            result.append(row.pop(0))
    return ''.join(result)