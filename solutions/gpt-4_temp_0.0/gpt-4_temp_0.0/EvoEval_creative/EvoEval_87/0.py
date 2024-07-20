def word_spiral(arr):
    if not arr:
        return ''
    result = []
    while arr:
        result += arr.pop(0)
        if arr and arr[0]:
            for row in arr:
                result.append(row.pop())
        if arr and arr[-1]:
            result += arr.pop()[::-1]
        if arr and arr[0]:
            for row in arr[::-1]:
                result.append(row.pop(0))
    return ''.join(result)