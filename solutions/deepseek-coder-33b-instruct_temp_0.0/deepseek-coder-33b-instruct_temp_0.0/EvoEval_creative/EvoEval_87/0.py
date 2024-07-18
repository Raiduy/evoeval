def word_spiral(arr):
    if not arr:
        return ''
    res = []
    while arr:
        res.extend(arr.pop(0))
        if not arr:
            break
        for row in arr:
            res.append(row.pop())
        res.extend(arr.pop()[::-1])
        if not arr:
            break
        for row in arr[::-1]:
            res.append(row.pop(0))
    return ''.join(res)